# Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로서 할 수 있는 작업들
# 3. HTTP 요청 전후에 대한 핸들러 관리

# - HTTP 요청을 실행하기 이전에 어떤 추가 작업을 실행하고자 한다면, 뷰 함수 안에 추가적으로 실행해야 할 로직을 기술하는 것이 일반적임
# - 하지만 이와 같은 처리가 여러 개 뷰 함수에 적용되야 한다면 사용하기 어렵다.
# - 자바는 이런 상황을 AOP를 사용하여 해결
# - Flask는 HTTP 요청 전후에 사용할 수 있는 데코레이터를 제공
#  1) before_first_request : 웹 애플리케이션 기동 이후 가장 처음에 들어오는 HTTP 요청에서만 실행됨
#  2) before_request : 매 HTTP 요청이 들어올 때 마다 실행됨
#  3) after_request : 매 HTTP 요청이 끝나 브라우저에 응답하기 전에 실행됨
#  4) teardown_request : HTTP 요청의 결과가 브라우저에 응답한 다음 실행됨
#  5) teardown_appcontext : HTTP 요청이 완전히 완료되면 실행됨. 애플리케이션 컨텍스트 내에서 실행됨

# - 데코레이터를 사용하는 함수들은 여러 개를 선언할 수 있고, HTTP 요청 전후에 호출되는 함수를 선언하지 않아도 된다.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def http_prepost_response():
    return "/"


# HTTP 요청 전에 실행되는 함수는 어떠한 인자도 전달할 수 없음
# before_first_request 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서 before_first_request_funcs 리스트 타입 변수에
# 요소로 추가되어 저장됨
@app.before_first_request
def before_first_request():
    print("앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답됨")


# HTTP 요청 전에 실행되는 함수는 어떠한 인자도 전달할 수 없음
# before_request 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서 before_request_funcs 리스트 타입 변수에
# 요소로 추가되어 저장됨
@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되기 전에 실행됨")


# after_request는 HTTP 요청이 처리되고 나서 브라우저에 응답하기 직전에 호출됨
# 이에 따라 해당 함수는 response 객체 인자를 받고 response 객체를 브라우저에 반환하기 직전까지 해야 할 어떤 일을
# 수행하면 된다.
# response 객체는 flask.wrapper.Response 클래스의 인스턴스이다.
# 함수에서 response 객체를 return문을 사용해 반드시 반환해야 한다. (그렇지 않으면 500 에러 발생)
# 해당 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서 after_request_funcs 리스트 타입 변수에 요소로 추가됨
@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리되고 나서 실행됨")
    return response


# teardown_request는 실행 순서 상 after_request 데코레이터를 사용하는 함수가 Flask에 의해 호출된 다음에 호출되는 데코레이터임
# teardown_request 데코레이터를 사용한 함수는 개별 HTTP 요청이 끝난 다음 반드시 실행되어야 하는 로직을 포함해야 한다.
# teardown_request 데코레이터를 사용한 함수는 예외 정보가 들어 있는 exception 인자를 반드시 전달 받아야 한다.
# teardown_request 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서 teardown_request_funcs 리스트 타입 변수에
# 요소로 추가됨
@app.teardown_request
def teardown_request(exception):
    print("매 HTTP 요청의 결과가 브라우저에 응답하고 나서 호출됨")


# teardown_appcontext는 teardown_request 다음에 호출되는 데코레이터임
# teardown_appcontext 데코레이터를 사용한 함수는 개별 HTTP 요청의 처리가 완전히 끝나고 Flask 애플리케이션 컨텍스트가
# 끝날 때 마다 실행됨
# 애플리케이션 코드에서는 `with app.app_context()` 블록 안에서 사용된 객체를 제거해야 할 때 등 제한적인 용도로 사요됨
# teardown_appcontext 데코레이터를 사용한 함수는 예외 정보가 들어 있는 exception 인자를 반드시 전달 받아야 한다.
# teardown_appcontext 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서 teardown_appcontext_funcs 리스트 타입 변수에
# 요소로 추가됨
@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행됨")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
