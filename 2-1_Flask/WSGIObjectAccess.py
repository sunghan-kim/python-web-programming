# Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로서 할 수 있는 작업들
# 5. 미들웨어 등록을 위한 순수 WSGI 객체 접근

# 웹 서버와 웹 프로그램 간의 통신 과정
#  - 웹 브라우저가 웹 서버에 요청
#  - 웹 서버가 요청에 따른 적절한 응답을 생성해 웹 브라우저에 응답을 반환하고 통신을 끊음
# 이런 과정에서 세션 처리나 쿠키 처리 등 HTTP 요청 전후에서 반드시 이루어져야 하는 일을 직접 작성하기는 어렵다.

# 이러한 HTTP 통신 과정에서의 요청과 응답으로 구성된 하나의 처리는 하나의 독립된 응용 애플리케이션으로 볼 수 있다.
# 파이썬의 웹 서버 인터페이스 규격인 WSGI(PEP 3333)에서는 이런 일들을 수행하는 계층을 "미들웨어(Middleware)"라고 부른다.

# 미들웨어는 여러 개를 추가할 수 있고 추가한 순서에 따라 순차적으로 적용된다.
# 미들웨어는 미들웨어 스택(파이썬 리스트 타입으로 관리)으로 관리된다.

# 미들웨어가 HTTP 통신 과정에서 처리할 수 있는 다양한 일
#  - 타깃 URL에 따른 애플리케이션 기동에 필요한 HTTP 환경(Environ) 재설정 및 Request Path 재설정
#  - 다수의 애플리케이션 또는 다른 프레임워크의 프로그램을 같은 프로세스에서 동작시키기
#  - 네트워크의 대역폭 분산 처리를 위해 로드 밸런싱과 원격 처리
#  - 컨텐츠의 전처리 (ex. XSL Stylesheet 적용 등)


# 로깅 미들웨어 선언 (http://www.flask.moe/source)
#  - 환경 변수 일부 값을 참조하여 로그 기록을 남기는 예제
#  - 이 미들웨어는 웹 브라우저가 접근하는 URL에 대해서 URL 전체와 쿼리를 분리해 로거에 전달하고, wsgi 객체를 반환하여
#    다음 미들웨어가 추가될 수 있도록 해야 한다.
#  - 사용자 미들웨어는 생성자 메서드(__init__)와 호출 메서드(__call__)를 반드시 포함해야 한다.
#  - 각각의 메서드는 정해진 인자를 받도록 선언한다.
#    - 생성자 메서드 : wsgi app 객체(app)
#    - 호출 메서드 : HTTP 환경 객체(environ), 응답 시작 객체(start_response)

from urllib.parse import unquote_plus
import logging


# 미들웨어 클래스의 이름은 관례적으로 Middleware를 덧붙여서 정한다.
# 파이썬의 모든 클래스는 상속 클래스를 명시적으로 지정하지 않은 경우는 object 클래스를 상속받게 된다.
# 여기서는 object 클래스를 상속 받는다고 명시적으로 지정했다.
class LogMiddleware(object):
    """WSGI middleware for collecting site usage"""

    # 미들웨어의 생성자를 선언
    def __init__(self, app):
        # 인자로 받은 Flask의 wsgi 인스턴스 객체는 미들웨어 클래스의 인스턴스 객체에 저장됨
        self.app = app

    # 호출 메서드 선언
    # 호출 메서드는 인스턴스화된 객체를 함수처럼 사용하기 위해 정의하는 클래스 특별 메서드이다.
    # 호출 메서드 이름은 반드시 "__call__"을 사용해야 한다.
    def __call__(self, environ, start_response):
        # HTTP 환경 객체로부터 "PATH_INFO"를 가져옴
        # PATH_INFO는 웹 브라우저가 접근 중인 URL 정보(스키마+호스트+포트+자원주소)를 모두 포함하고 있다.
        url = environ.get("PATH_INFO", "")

        # HTTP 환경 객체로부터 "QUERY_STRING"을 가져옴
        # QUERY_STRING은 URL 뒤에 "?(물음표)"로 시작하는 문자열들을 의미한다.
        # 이 문자열은 "키=값"의 형태로 연관지어 "&"문자로 연결되어 있다.
        # 이 정보는 일반적으로 웹 브라우저가 웹 애플리케이션의 자원에 요청할 때 응답을 생성하기 위해 웹 애플리케이션이 참조할 정보이다.
        query = unquote_plus(environ.get("QUERY_STRING", ""))

        # 로깅 모듈의 LogRecord 클래스로부터 인스턴스 객체를 생성
        # LogRecord는 프로그래머가 전달한 로그 내용을 수정하는 데 사용
        item = logging.LogRecord(
            name="Logging",
            level=logging.INFO,
            pathname=url,
            lineno="",
            msg=query,
            args=None,
            exc_info=None
        )

        # metrics_logger 객체의 handle 메서드에 위에서 생성한 LogRecord 인스턴스 객체를 전달
        # handle 메서드는 LogHandler가 하나의 로그 레코드를 어떻게 구성할 지에 대한 정보이다.
        metrics_logger.handle(item)

        # 실행될 미들웨어를 위해 wsgi 객체를 반환
        # wsgi 객체를 반환할 때는 반드시 wsgi 객체에 environ 인자와 start_response를 인자로 전달한 값을 반환해야 한다.
        return self.app(environ, start_response)


# 이제 이렇게 작성된 미들웨어는 Flask로 작성된 웹 애플리케이션에 등록해야 한다.
# 등록이 완료되면 미들웨어는 HTTP 요청 전후에 호출되어 처리된다.

# 미들웨어 등록
from flask import Flask

app = Flask(__name__)

# 미들웨어 등록은 Flask 인스턴스 객체의 속성인 wsgi_app를 미들웨어 클래스의 생성자에 전달하고, 미들웨어 클래스의
# 호출 메서드가 반환한 wsgi 객체를 Flask 인스턴스 객체의 wsgi_app에 재할당하는 것으로 등록 절차를 마친다.
app.wsgi_app = LogMiddleware(app.wsgi_app)


# 미들웨어가 하는 일은 before_request, after_request 데코레이터 역할과 같다.
# 다만, 미들웨어는 웹 서버와 웹 애플리케이션 사이에서 동작하는 것이 가장 큰 차이이다.
