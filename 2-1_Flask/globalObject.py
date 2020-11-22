# Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로서 할 수 있는 작업들
# 1. 글로벌 객체

# - 파이썬은 언어 특성 상 전역 영역은 애플리케이션 전체에 걸친 영역이 아닌 모듈 단위의 영역으로 한정한다.
# - Flask는 전역적으로 데이터를 보관하고 사용할 수 있도록 글로벌 객체를 제공한다.

# flask 객체로부터 글로벌 객체 가져오기
# - g 객체는 Flask 인스턴스 객체의 app_ctx_globals_class 클래스의 인스턴스 변수이다.
from flask import g
import sqlite3
from flask import Flask

app = Flask(__name__)


# - 일반적으로 Flask에서 제공하는 글로벌 객체는 웹 애플리케이션이 동작하는 동안 유지되어야 하는 값을 저장한다.
#  - ex) 데이터베이스 연결 객체

# 글로벌 객체 사용
# - 개별 HTTP 요청을 웹 애플리케이션이 받아 처리하기 전에 Flask 글로벌 객체에 데이터베이스 연결을 담아두고,
#   요청이 모두 처리되어 응답할 때 데이터베이스 연결을 종료

# DB 연결 함수 선언
def connect_db():
    # sqlite3 모듈의 connect 함수를 이용해 데이터베이스에 연결 시도 및 생성된 DB 연결 객체 반환
    # 데이터베이스 연결에 시도하는 설정값은 Flask 인스턴스 변수의 환경 설정 객체(config 객체)에 DATABASE 키 값으로 저장되어 있음
    return sqlite3.connect(app.config['DATABASE'])

# 웹 브라우저로부터 HTTP 요청이 들어올 때 마다 데이터베이스 연결 객체를 글로벌 객체에 저장
# before_request 데코레이터
# - HTTP 요청이 올 때마다 실행됨
# - before_request 데코레이터를 이용한 함수는 Flask 애플리케이션 내에서 여러 개를 선언할 수 있음
@app.before_request
def before_request():
    g.db = connect_db()

# Flask 애플리케이션에서 HTTP 요청의 처리가 완료될 때 호출되는 함수 선언
# teardown_request 데코레이터
# - HTTP 요청이 처리되는 시점인 HTTP 응답이 이뤄질 때 호출되어 처리됨
@app.teardown_request
def teardown_request(exception):
    # 데이터베이스 연결 객체를  getattr 함수를 이용해 Flask 글로벌 객체에서 db 속성을 가져옴
    # 찾지 못하면 None을 반환 (세 번째 파라미터)
    db = getattr(g, 'db', None)

    # db 속성값이 None이 아닌 경우, db 속성(데이터베이스 연결 객체)의 close() 메서드를 호출해 데이터베이스 연결 종료
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")