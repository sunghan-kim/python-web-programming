# Flask에서는 HTTP 요청과 응답을 처리하기 위해 Request 객체와 Response 객체를 제공한다.
# HTTP 요청은 flask 모듈에서 proxy화된 Request 클래스를 가져와서 사용하는 것이 일반적이다.

# GET 방식에서 넘어온 쿼리 스트링에서 question 변수 값 가져오기
from flask import Flask, request

app = Flask(__name__)


@app.route('/board')
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다.".format(request.args.get('question'))


# 이 코드를 웹 브라우저에서 확인하려면 다음과 같은 URL을 호출하면 된다.
#  - http://localhost:5000/board?question=answer

# request 클래스는 HTTP 메시지를 사용하기 쉬운 형태로 반환해주는 여러 헬퍼 메서드와 속성을 제공한다.

# 1. 웹 브라우저가 보는 데이터(ex. 쿼리 스트링, HTTP 메시지 바디, 첨부 파일 등)에 효출적으로 접근하는 방법
#  - HTTP 메서드 중 GET, POST 방식으로 전송된 데이터는 Flask에서 werkzeug.datastructures.MultiDict 데이터 타입으로 저장된다.
#  - GET 방식으로 전달된 데이터는 request 클래스의 args 속성을 통해 웹 브라우저가 전송한 데이터를 가져올 수 있다.
#    (단, GET 방식으로 전달된 데이터만 args 속성으로 접근할 수 있다.)

# GET 방식의 쿼리 스트링에 접근하기
@app.route('/board2')
def board2():

    # get 메서드의 인자들
    #  1) 가져올 쿼리 변수명
    #  2) default 값
    #  3) 타입
    article_id = request.args.get('article', '1', int)
    return str(article_id)



if __name__ == '__main__':
    app.run(host='127.0.0.1')