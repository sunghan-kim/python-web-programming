from flask import Flask

app = Flask(__name__)


# 뷰 함수에 별칭 지정하기
# - 뷰 함수의 별칭을 특별히 지정하지 않으면 뷰 함수의 이름이 암시적으로 사용됨
# - 이 별칭은 url_for 함수에서 뷰 함수를 식별하기 위한 이름으로 사용함
# - 별칭의 지정은 route 데코레이터 또는 add_url_rule 함수에 endpoint 인자로 전달하면 됨
@app.route('/board4', endpoint='board4')
def board():
    return ""


# '/'에 대한 URL 뷰 함수만 구현되어 있는 상황에서 '/guestbook' URL 호출 시
# -> 404 상태 코드(Not Found) 응답

# '/board' URL에 대한 뷰 함수가 GET 요청만 응답하도록 구현되어 있는 상황에서 '/board/' URL을 POST 메서드로 호출한 경우
# -> 405 상태 코드(Method Not Allowed) 응답

if __name__ == '__main__':
    app.run()