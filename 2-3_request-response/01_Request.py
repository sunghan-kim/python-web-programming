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
#  - GET : request.args
#  - POST : request.form

# 1-1. GET 방식의 쿼리 스트링 접근
#  - GET 방식으로 전달된 데이터(ex. 쿼리 스트링)는 request 클래스의 args 속성을 통해 웹 브라우저가 전송한 데이터를 가져올 수 있다.
#    (단, GET 방식으로 전달된 데이터만 args 속성으로 접근할 수 있다.)
@app.route('/board2')
def board2():

    # get 메서드의 인자들
    #  1) 가져올 쿼리 변수명
    #  2) default 값
    #  3) 타입
    article_id = request.args.get('article', '1', int)
    return str(article_id)


# 1-2. form 속성을 통해 데이터 접근
#  - POST 방식으로 전달된 데이터는 request 객체에서 form 속성을 통해 읽어올 수 있다.
#  - form 속성을 통해 웹 브라우저가 보내온 데이터를 읽기 위해서는 웹 브라우저가 HTTP 메시지 헤더인
#    Content-Type의 헤더 값으로 데이터를 인코딩해서 보내는 방식으로 application/x-www-form-urlencoded가 지정되어야 한다.

#  - GET 방식으로 넘어 온 쿼리 스트링이 있다면 쿼리 스트링으로 전달된 변수값은 form 속성을 통해 접근할 수 없다.
#  - POST 방식의 데이터를 읽어오기 위해서는 웹 애플리케이션과 HTTP 헤더에 다음 2가지를 설정해야 한다.
#   1) 라우팅 옵션인 methods에 "POST" 값 추가
#   2) HTTP 메시지에 HTTP 헤더인 "Content-Type"에 "application/x-www-form-urlencoded" 값 지정
@app.route('/board3', methods=['POST'])
def board3():
    article_id = request.form.get('article', '1', int)
    return str(article_id)


# 1-3. values 속성을 통해 데이터 접근
#  - request 객체의 values 속성은 웹 브라우저가 GET 또는 POST 메서드로 보냈을 때 HTTP 메서드 타입에 상관없이
#    보낸 데이터를 읽어올 수 있다.
#  - 주의 사항
#    - GET과 POST가 동일한 변수명을 가진 데이터를 보내게 되면 GET 메서드로 보낸 데이터가 우선된다.
#  - values 속성은 CombinedMultiDict 데이터 타입이다.
#    - MultiDict 데이터 타입들이 합쳐진 형태
#    - 이 타입은 MultiDict 타입들의 Wrapper로서만 동작하므로 실제로 데이터에 접근하는 메서드는 MultiDict 타입의 메서드로 대신 제공한다.
@app.route('/board4', methods=['GET', 'POST'])
def board4():
    return request.values.get('question')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
