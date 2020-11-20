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

from flask import Flask

app = Flask(__name__)


@app.route("/")
def http_prepost_response():
    return "/"


@app.before_first_request
def before_first_request():
    print("앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답됨")


@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되기 전에 실행됨")


@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리되고 나서 실행됨")
    return response


@app.teardown_request
def teardown_request(exception):
    print("매 HTTP 요청의 결과가 브라우저에 응답하고 나서 호출됨")


@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행됨")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
