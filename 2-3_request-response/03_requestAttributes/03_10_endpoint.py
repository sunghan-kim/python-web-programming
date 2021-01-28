# request.endpoint 속성
#  - endpoint 속성은 웹 브라우저가 처리를 요청한 "뷰 함수의 별칭"을 확인할 수 있다.
#  - endpoint 이름은 별도로 지정하지 않으면 뷰 함수의 이름이 된다.
#    - ex) Blueprint 이름 = flask, endpoint = hello
#       -> flask.hello 와 같은 형태의 이름이 저장됨

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/environ', methods=['GET', 'POST'])
def example_environ():
    return request.endpoint

app.run()
