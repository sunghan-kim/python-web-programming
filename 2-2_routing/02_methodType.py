# HTTP 메서드 타입
# - 브라우저가 HTTP 서버에 URL을 호출하는 세부적인 방법
# - 종류 : GET, POST, PUT, DELETE 등

# GET 메서드
# - 자원의 위치(URI)와 쿼리 스트링(?~~~)을 함께 전달
# - 웹 브라우저의 주소 줄에 정보가 노출됨

# POST 메서드
# - HTTP 메시지의 바디에 데이터를 포함해 전달
# - 웹 서버가 HTTPS를 운영 중이면 웹 브라우저가 보내는 모든 요청은 암호화됨
# - 그렇기 때문에 중요 정보를 전달하고 웹 프로그램의 데이터를 변경하는 목적으로 사용됨

from flask import Flask

app = Flask(__name__)


@app.route('/board', methods=['GET'])
def board_list_get():
    return ""


@app.route('/board', methods=['POST'])
def board_list_post():
    return ""


# 하나의 뷰 함수가 여러 HTTP 메서드 타입을 처리할 수도 있음
@app.route('/board2', methods=['GET', 'POST'])
def board_list2():
    return ""


# route 데코레이터에 methods 인자가 없으면 뷰 함수는 GET 요청만 처리한다.
@app.route('/board3')
def board_list3():
    return ""





if __name__ == "__main__":
    app.run()
