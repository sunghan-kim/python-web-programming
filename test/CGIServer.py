# CGI 서버 실행
# - CGI 서버
#   - 정적인 파일만 서비스하는 웹 서버가 아닌 CGI 스크립트를 지원하도록 하는 내장 웹 서버
#   - CGI 서버의 실행은 정적인 웹 서버와 달리 CGI 스크립트가 있는 디렉터리를 생성해야 함

# 명령어
# cd ./test/cgi-server
# python -m http.server --cgi 8080

# 파이썬 스크립트로 CGI 서버 실행하기
import http.server
import socketserver

PORT = 8080

Handler = http.server.CGIHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

# CGI 스크립트가 동작하는 서버와 포트 번호를 소켓 서버 객체에 추가
httpd.server_name = "localhost"
httpd.server_port = PORT

print("serving at port", PORT)
httpd.serve_forever()