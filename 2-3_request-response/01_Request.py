# Flask에서는 HTTP 요청과 응답을 처리하기 위해 Request 객체와 Response 객체를 제공한다.
# HTTP 요청은 flask 모듈에서 proxy화된 Request 클래스를 가져와서 사용하는 것이 일반적이다.

# GET 방식에서 넘어온 쿼리 스트링에서 question 변수 값 가져오기
from flask import Flask, request

app = Flask(__name__)


@app.route('/board')
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다.".format(request.args.get('question'))


if __name__ == '__main__':
    app.run(host='127.0.0.1')


# 이 코드를 웹 브라우저에서 확인하려면 다음과 같은 URL을 호출하면 된다.
#  - http://localhost:5000/board?question=answer
