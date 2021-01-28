# request.view_args 속성
#  - URL 변수를 확인해볼 수 있는 속성
#  - 이 속성의 데이터 타입 : 딕셔너리
#  - URL 변수를 웹 브라우저로부터 넘겨받을 경우
#    - key : URL Rule에 지정된 URL 변수명
#    - value : 변수로 받기로 한 위치에 전달된 값

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/rule/<name>', methods=['GET', 'POST'])
def example_environ(name):
    print(request.view_args)
    return ''

app.run()
