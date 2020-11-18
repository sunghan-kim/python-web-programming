# Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로서 할 수 있는 작업들
# 2. 사용자 응답 객체 생성

# - 다수의 응답에 공통적으로 적용해야 할 응답 헤더를 추가해야 할 때 사용자 응답 객체를 정의하여 사용
# - 사용자 응답 객체를 반환하기 위해서는 flask 모듈의 make_response 함수 이용
# - make_response 함수는 5가지의 사용자 응답 객체를 지원

# Flask가 지원하는 5가지 사용자 응답 객체
#  1) response_class : Response 클래스(또는 자식 클래스)로부터 생성한 인스턴스 객체
#  2) str : 유니코드가 아닌 일반 문자열
#  3) unicode : 유니코드 문자열 (unicode 데이터 타입은 파이썬 2 버전에만 존재)
#  4) WSGI 함수 : 프로그래머가 정의한 WSGI 함수는 호출되면 버퍼링된 응답 객체로 반환됨
#  5) 튜플(tuple)
#   - (response, status, headers) 형식을 갖춘 튜플을 인자로 제공받음
#     - response : response_class, str, unicode, WSGI 함수 중 하나만 올 수 있음
#     - status :  HTTP 상태 응답 코드 또는 HTTP 상태 오류 메시지
#     - headers : HTTP 헤더를 파이썬 사전 형식으로 제공


# Flask의 기본 응답 객체로 사용되는 Response 클래스로부터 인스턴스 객체를 생성하고 브라우저에 응답
from flask import Response, make_response
from helloworld import app


# 1) response_class 응답 객체 생성
@app.route("/response_class")
def response_test1():
    custom_response = Response("Custom Response",  # 웹 브라우저에 "Custom Resposne"라는 문자열 반환
                               200,  # HTTP 상태 코드 값을 200으로 설정하여 브라우저의 요청이 성공적으로 처리되었음을 알림
                               {
                                   # HTTP 응답 메시지 헤더에 "Program" 키와 키 값에 "Flask Web Application"을 설정
                                   "Program": "Flask Web Application"
                               })
    return make_response(custom_response)


# 2) str 문자열 사용
#  - 문자열을 응답 객체로 사용하는 경우는 HTTP 응답 헤더 조정이나 HTTP 응답 상태 코드 수정 등의 일을 수행할 수 없음
#  - 해당 기법은 실제 개발 환경에서 사용 빈도가 적고, make_response 함수를 사용하지 않고 응답을 반환하는 경우가 더 많음
@app.route("/str")
def response_test2():
    return make_response("Custom Response")


# 3) unicode 문자열 사용 (파이썬 2 버전에서만 동작)
#  - 유니코드 문자열을 사용하여 웹 브라우저에 응답하는 방법
#  - 파이썬 3 이상에서는 모든 문자열을 유니코드로 취급하기 때문에 2) 방법과 같이 일반 문자열을 사용해도 유니코드 문자열을 반환함
#  - 유니코드 표시 (파이썬 2 에서)
#   - 문자열 인용 기호(", ') 앞에 u 붙이기
#   - 문자열을 unicode 함수로 감싸기
@app.route("/unicode")
def response_test3():
    return make_response(u"Custom Response")


# 4) WSGI function 사용
#  - WSGI 함수를 응답 객체로 사용
#  - WSGI는 함수로 선언하여 사용하는 것이 일반적 (클래스로 정의하여 사용하는 경우도 있음, WSGI-class.py 참고)
#  - WSGI 함수를 사용하여 응답하면 보다 정교하게 HTTP 응답을 제어할 수 있어서 고급 응용 프로그램에서는 자주 이용되는 기법 중 하나
#  - 하지만 대부분의 경우 앞서 설명된 방법들을 주로 이용하게 됨
@app.route("/WSGI")
def custom_response():

    # WSGI 함수 정의 시작
    #  - environ : 웹 서버 환경 설정값을 갖고 있는 딕셔너리
    #  - start_response : 웹 브라우저에 응답을 반환하기 위한 함수 객체
    def application(environ, start_response):

        # 웹 브라우저에 응답할 문자열 생성
        #  - environ['REQUEST_METHOD'] : 웹 브라우저가 URL을 어떤 메서드로 호출했는 지가 저장됨
        #  - 현재 "/WSGI" URL은 GET 메서드로만 호출이 가능함
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']

        # HTTP 응답의 상태 값을 상태 코드와 메시지로 저장
        status = '200 OK'

        # HTTP 응답 메시지의 헤더 구성
        #  - 리스트로 구성
        #  - 아이템의 요소는 헤더 키와 값으로 구성된 튜플 객체들
        response_headers = [
            # Content-Type : 응답하는 문자열이 Plain Text(평문) 문자열임을 알리는 헤더
            ('Content-Type', 'text/plain'),
            # Content-Length : 컨텐츠의 길이를 문자열로 지정한 헤더
            ('Content-Length', str(len(response_body)))
        ]

        # start_response 함수 객체에 HTTP 응답 상태 코드(status)와 HTTP 응답 헤더(response_headers)를 전달하여
        # 웹 브라우저에 응답을 시작
        start_response(status, response_headers)

        # 웹 브라우저에 응답할 문자열을 리스트로 감싸 반환환
        return [response_body]

    return make_response(application)


# 5) 튜플(tuple)
#  - 튜플 형태로 구성된 응답
#  - 튜플로 구성된 객체의 인자들
#   (1) 응답 객체(response_class, 일반 또는 유니코드 문자열, wsgi 함수)
#   (2) HTTP 상태 코드 값(ex. 200) or HTTP 상태 코드 문자열(ex. OK)
#   (3) 응답 헤더를 딕셔너리 타입으로 전달
#  - 튜플로 웹 브라우저에 응답할 내용을 make_response 함수에 인자로 전달하는 것은
#    응답 상태 코드나 헤더의 내용을 조정하기에 편리하다.
@app.route("/tuple")
def custom_response2():
    return make_response(('Tuple Custom Response', 'OK', {'response_method': 'Tuple Response'}))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
