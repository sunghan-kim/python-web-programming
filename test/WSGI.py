from wsgiref.simple_server import make_server


# wsgi 함수
def application(environ, start_response):
    # environ : CGI 환경 변수를 담고 있는 변수
    # start_response : 웹 브라우저에 응답을 반환하는 변수
    response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)

    status = '200 OK'

    # 웹 브라우저에 응답할 HTTP 메시지 헤더 구성
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)

    # application 함수를 호출한 WSGI 서버에게 웹 브라우저에게 응답할 문자열을 요소값으로 가지는 파이썬 리스트 반환
    # 모든 CGI 환경 변수의 이름과 변수가 가지고 있는 값 리턴
    return [response_body.encode('utf8')]


httpd = make_server('localhost', 8051, application)
httpd.handle_request()

# 웹 브라우저에서 "http://localhost:8051" 로 접속
# 이 URL은 http 프로토콜로서 localhost 서버의 8051 포트에 접속하라는 의미이다.
