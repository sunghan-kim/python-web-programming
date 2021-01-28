# request.method 속성
#  - method 속성은 웹 브라우저가 어떤 HTTP 메서드로 URL을 호출했는 지에 대한 정보가 저장되어 있다.
#  - 이 속성은 HTTP 환경 변수의 REQUEST_METHOD 키를 통해서도 확인 가능하다.

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/environ', methods=['GET', 'POST'])
def example_environ():
    return request.method

app.run()
