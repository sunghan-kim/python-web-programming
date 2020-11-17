# 파이썬 내장 웹 서버 실행 스크립트
import http.server
import socketserver

PORT = 8080

# PORT로 들어오는 요청을 http.server 모듈의 SimpleHTTPRequestHandler가 처리할 것임을 명시
Handler = http.server.SimpleHTTPRequestHandler

# scoketserver 모듈의 TCPServer 클래스 인스턴스화
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)

# 소켓 서버 실행
# 소켓 서버가 PORT로 들어오는 연결을 계속해서 감시하도록 하는 데 사용
httpd.serve_forever()