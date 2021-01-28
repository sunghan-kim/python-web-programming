# request.environ 속성
#  - environ 속성은 HTTP 통신에서 사용되는 환경 변수를 담고 있는 딕셔너리이다.
#  - 이 딕셔너리에서 참조할 수 있는 환경 변수의 종류
#    1) 표준 환경 변수
#    2) wsgi 전용 환경 변수


# WSGI에서 제공하는 표준 환경 변수 및 WSGI 환경 변수 값 확인
from flask import Flask, request

app = Flask(__name__)

@app.route('/example/environ', methods=['GET', 'POST'])
def example_environ():
    ret_str = (
        'REQUEST_METHOD: %(REQUEST_METHOD)s<br>' 
        # REQUEST_METHOD
        #  - 웹 브라우저가 보낸 요청의 처리 방식에 대한 문자열
        'SCRIPT_NAME: %(SCRIPT_NAME)s<br>'
        # SCRIPT_NAME
        #  - 애플리케이션에서 처리를 요청한 URL의 첫 부분
        #  - PHP 등의 스크립트 언어에서 이 변수값은 스크립트 파일명이 된다.
        #  - Flask에서는 빈 값으로 출력되는 경우가 많다.
        'PATH_INFO: %(PATH_INFO)s<br>'
        # PATH_INFO
        #  - 웹 브라우저가 처리를 요청한 URL에서 자원이 위치한 경로(PATH) 부분
        'QUERY_STRING: %(QUERY_STRING)s<br>'
        # QUERY_STRING
        #  - 쿼리 스트링 : URL 맨 끝에 "?" 문자 뒤에 오는 문자열
        #  - 쿼리 스트링을 URL에 추가하지 않고 URL을 호출하면 이 변숫값의 내용은 비어 있음
        #'CONTENT_TYPE: %(CONTENT_TYPE)s<br>'
        # CONTENT_TYPE
        #  - 웹 브라우저가 보낸 HTTP 요청 메시지의 바디에 포함되는 컨텐츠 형태가 저장되어 있음
        #  - HTTP 메시지 헤더에 있는 Content-Type 헤더의 값을 확인할 수 있음
        #  - GET 메서드 타입으로 보낸 HTTP 메시지에 바디가 없는 경우 이 값은 비어 있음
        #'CONTENT_LENGTH: %(CONTENT_LENGTH)s<br>'
        # CONTENT_LENGTH
        #  - 웹 브라우저가 보낸 HTTP 요청 메시지의 바디에 기록되어 있는 콘텐츠의 길이가 저장되어 있음
        #  - 숫자 타입의 값
        #  - 인코딩 타입에 상관없이 글자 한 개를 한 개의 길이로 계산
        #  - GET 메서드 타입으로 보낸 HTTP 메시지에 바디가 없는 경우 이 값은 비어 있음
        'SERVER_NAME: %(SERVER_NAME)s<br>'
        # SERVER_NAME
        #  - 서버의 도메인 주소(or IP)가 저장됨
        'SERVER_PORT: %(SERVER_PORT)s<br>'
        # SERVER_PORT
        #  - 웹 애플리케이션이 동작 중인 서버의 포트 번호가 저장됨
        #  - 도메인 주소에 포트 번호가 없으면 웹 서버가 응답할 것으로 기대되는 포트 번호인 80이 저장됨
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL)s<br>'
        # SERVER_PROTOCOL
        #  - 서버 프로토콜 버전이 표시됨
        #  - "HTTP/1.0" or "HTTP/1.1"
        # HTTP_Variables
        #  - 반드시 필요한 헤더를 제외하고 웹 브라우저가 전송한 모든 헤더의 값을 저장하고 있음
        #   - ex) User-Agent 헤더 전송 -> HTTP_USER_AGENT 속성값으로 확인
        'wsgi.version: %(wsgi.version)s<br>'
        # wsgi.version
        #  - WSGI 버전을 튜플 타입으로 반환
        #  - 1.0 버전 -> (1, 0) 이 반환됨
        'wsgi.url_scheme: %(wsgi.url_scheme)s<br>'
        # wsgi.url_scheme
        #  - URL의 스키마 종류가 저장되어 있음
        #  - 웹 서버인 경우 항상 "http"를 반환
        'wsgi.input: %(wsgi.input)s<br>'
        # wsgi.input
        #  - HTTP 요청 메시지의 바디를 '파일 객체'로 읽을 수 있도록 파일 유사 객체가 저장되어 있음
        'wsgi.errors: %(wsgi.errors)s<br>'
        # wsgi.errors
        #  - HTTP 요청에서 오류가 발생했을 경우 오류 내용을 '파일 유사 객체'로 읽을 수 있도록 파일 유사 객체가 저장되어 있음
        'wsgi.multithread: %(wsgi.multithread)s<br>'
        # wsgi.multithread
        #  - 현재 요청이 멀티스레드에서 동작할 수 있는 지를 boolean 값으로 반환
        'wsgi.multiprocess: %(wsgi.multiprocess)s<br>'
        # wsgi.multiprocess
        #  - 현재 요청이 멀티프로세스에서 동작할 수 있는 지를 boolean 값으로 반환
        'wsgi.run_once: %(wsgi.run_once)s<br>'
        # wsgi.run_once
        #  - 현재 요청이 한 번만 실행되는 지를 boolean 값으로 반환
    ) % request.environ
    return ret_str

if __name__ == '__main__':
    app.run()
