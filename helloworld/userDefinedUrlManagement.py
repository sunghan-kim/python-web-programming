# Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로서 할 수 있는 작업들
# 4. 사용자 정의 URL 처리 함수 관리

# URL은 URI의 한 종류이다.
# URL의 일반적인 구성
#  - /board_view.jsp?id=35&page2&key=title&value=
# 2005년 이후 등장한 사용자 친화적인 형태의 URL
#  - /board/35?page2&key=title&value=
# 위 URL은 게시판에서 35번 게시물을 가져와서 보여달라는 의미
# 사이트 방문자가 기억하기 쉬운 형태로 구성되어 있음
# 이 때 URL(사용자가 요청하는 자원의 주소)의 한 부분으로 취급되는 35라는 값을 뷰 함수에 인자로 전달함으로써 뷰 함수에서 쉽게 참조할 수 있다.

# Flask에서는 URL의 일부로 다뤄지는 파라미터(여기서는 35)를 프로그래머가 뷰 함수 내에서 객체 또는 특정한 결과로
# 반환받을 수 있는 방법을 제공하고 있다.

# URL의 일부로 다뤄지는 인자 값을 객체로 반환하기 (일부 코드는 생략됨)
#  - URL의 일부를 사용자 정의 컨버터(custom converter)를 이용해 객체로 변환해서 처리

# 컨버터 클래스를 선언하기 위해 기본이 되는 BaseConverter 클래스를 불러옴
from werkzeug.routing import BaseConverter
from models import Board
from database import db_session
from flask import Flask, url_for


# 컨버터 클래스 선언 시작
class BoardView(BaseConverter):
    # URL의 일부로 넘어온 인자 값은 to_python 메서드에 value 인자로 전달됨
    def to_python(self, value):
        # 전달된 인자를 DB에 질의해서 첫 번째로 검색된 레코드를 가져옴
        record = db_session.query(Board).filter(Board.id == value).first()
        # 검색된 레코드를 뷰 함수에 인자로 전달
        return record

    def to_url(self, record):
        return record.id


app = Flask(__name__)
# 프로그래머가 생성한 URL 컨버터를 Flask 인스턴스 객체의 url_map.converters 딕셔너리에 board 이름으로
# 참조할 수 있도록 BoardView 클래스를 저장
app.url_map.converters['board'] = BoardView


# 웹 브라우저가 접근하는 URL 매핑을 route 데코레이터를 이용해 선언
# 게시물 번호 부분
#  - 산형 괄호(<, >)로 감싸고, 안의 내용은 콜론(:) 문자로 구분
#  - 앞 부분 : URL 컨버터명
#  - 뒷 부분 : 뷰 함수에 전달할 변수명 (여기서는 record라는 이름으로 받도록 지정
# url_for 함수에서 해당 URL을 쉽게 참조할 수 있도록 endpoint를 지정
@app.route("/board/<board:record>", endpoint="view")
# 뷰 함수 선언
# 해당 함수는 "/board/35" 라는 URL이 호출되면 실행됨
# "35" 라고 쓰여진 부분은 URL 컨버터에 의해서 35라는 값이 BoardView 클래스의 to_python 메서드에 전달되고,
# 임의의 파이썬 객체(여기서는 SQLAlchemy Model)를 반환하면 해당 객체를 뷰 함수에 인자로 전달함
# 이 떄 뷰 함수에 전달되는 인자의 이름은 위에서 정의한 이름(콜론(:)으로 나뉜 뒷부분)이 사용되어야 한다.
def board_view_route(record):
    # url_for 함수
    #  - 첫 번째 인자
    #    - 접근할 뷰 함수의 endpoint 이름을 지정
    #  - 두 번째 인자
    #    - 접근할 뷰 함수에 가변 인자를 키워드 인자로 전달
    #    - 해당 함수가 전달받은 record 변수가 이미 Board 모델 객체이기 때문에 record 인자에 전달받은 record 변수를 그대로 사용
    # 이렇게 하면 url_for 함수가 웹 브라우저에 전달한 URL 생성 과정 중 특정 URL 인자 형식을 처리하는 URL 컨버터의
    # to_url 메서드를 사용해 URL에 표현할 수 있는 문자, 숫자로 변환해서 그 결과를 반환한다.
    return url_for("view", record=record)


if __name__ == "__main__":
    app.run(host="0.0.0.0")


# URL 변수의 데이터 타입 변환 방법
#  - URL 컨버터 지정에 파이썬 기본 타입을 사용하는 방법
#  - 앞의 URL 컨버터를 사용하는 방법
#    - URL 컨버터를 사용하면 적은 양의 코드로 파이썬 객체를 뷰 함수에서 이용할 수 있으므로 생산성 향상 및 중복 코드 관리에 좋다.
