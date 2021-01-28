# request.url_rule 속성
#  - url_rule 속성은 현재 처리 중인 뷰 함수의 라우팅 URL Rule 을 확인해볼 수 있다.

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/rule', methods=['GET', 'POST'])
def example_rule():
    return str(request.url_rule)

app.run()
