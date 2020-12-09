# route 데코레이터와 add_url_rule 메서드의 키워드 인자

# 1) defaults
#  - 사용자 URL 변수에 기본값을 지정하는 옵션
#  - 딕셔너리 타입으로 전달

# 2) methods
#  - 뷰 함수가 처리할 HTTP 메서드 지정
#  - 문자열을 요솟값으로 가지는 리스트를 전달

# 3) host
#  - 라우팅 요청이 어떤 호스트에 응답할 지를 지정
#  - 문자열을 전달

# 4) subdomain
#  - 뷰 함수가 특정 서브 도메인에만 응답하도록 지정
#  - 문자열 타입으로 전달

# 5) redirect_to
#  - 라우팅 요청을 받았을 경우 뷰 함수가 처리하지 않고 다른 곳으로 요청을 전달
#  - 문자열 값 또는 리다이렉션 함수를 인자로 받음
#  - 리다이렉션 함수의 인자
#    - 변수값을 처리 할 어댑터
#    - 변수값

# 6) alias
#  - endpoint 옵션과 같은 역할을 하는 옵션

from flask import Flask

app = Flask(__name__)


# 1) defaults
#  - 이 코드로 생성하는 라우팅은 브라우저에 다음과 같이 호출하여 확인할 수 있다.
#    - http://localhost:5000/board (== http://localhost:5000/board/10, default 값이 10이기 때문)
#    - http://localhost:5000/board/20
@app.route('/board/<article_id>')
@app.route('/board', defaults={'article_id': 10})
def board(article_id):
    return '{}번 게시물을 보고 계십니다.'.format(article_id)


# 2) methods
#  - 가능한 옵션 인자
#    : GET, POST, HEAD, PUT, TRACE, CONNECT, DELETE, OPTIONS
#  - HTTP 메서드별로 HTTP 규약에서 정의된 목적이 있으므로 목적에 맞게 써야 한다.
#  - 필요한 경우 사용자 정의 HTTP 메서드를 만들어 사용할 수도 있다.
@app.route('/board', methods=['GET', 'POST'])
def board():
    return ''


# 3) host
#  - 라우팅 뷰 함수가 응답할 서버 도메인을 지정
#  - 라우팅 옵션 host를 지정해 특정 도메인 요청만 처리하게 할 수 있다.
#  - 이 옵션을 사용하기 전에 Flask 인스턴스 객체인 app의 url_map.host_matchinig 속성값을 True로 설정해야 한다.
app.url_map.host_matching = True

# - 라우팅이 처리할 도메인을 하나만 지정
@app.route('/board', host='example.com')
def board():
    return '/board URL을 호출했습니다.'


# - 라우팅이 처리할 도메인을 하나 이상 지정
@app.route('/board', host='example.com')
@app.route('/board', host='example2.com')
def board():
    return '/board URL을 호출했습니다.'

# - 만약 가상 호스트 5개가 하나의 Flask 애플리케이션을 가리키고 host 옵션이 지정되지 않으면,
#   뷰 함수는 모든 가상 호스트에 응답한다.


# 4) subdomain
#  - 기본 도메인이 같으면서 서브 도메인이 있는 경우 어떤 서브 도메인에 응답할 지 지정하는 데 사용
#  - subdomain 옵션은 이전의 다른 설정과 달리, Flask 인스턴스 변수의 설정 사전(config)에 애플리케이션이 동작해야 할 도메인을
#    서버 포트 번호와 함께 기술해서 SERVER_NAME 키에 문자열 타입으로 반드시 설정해야 한다.
app.config['SERVER_NAME'] = 'example.com:5000'


#  - 개별 라우팅에서 subdomain은 도메인 주소를 제외하고 서브 도메인 이름만 지정하는 것으로 서브 도메인별로 응답할 뷰 함수가
#    달라지게 된다.

@app.route('/board', subdomain='test')
def board_domain_test():
    return 'Test 도메인의 /board URL을 호출했습니다.'


@app.route('/board', subdomain='answer')
def board_domain_answer():
    return 'Answer 도메인의 /board URL을 호출했습니다.'


# - 특정 뷰 함수가 다수의 서브 도메인에 응답하게 할 경우에는 다음과 같이 지정할 수 있다.
app.config['SERVER_NAME'] = 'example.com:5000'


@app.route('/board', subdomain='test')
@app.route('/board', subdomain='answer')
def board_domain_testandanswer():
    return 'Test, Answer 도메인의 /board URL을 호출했습니다.'


# - 서브 도메인 종류에 상관없이 특정 뷰 함수가 응답하게 하려면 다음과 같이 지정할 수 있다.
app.config['SERVER_NAME'] = 'example.com:5000'


@app.route('/board', subdomain='<user_domain>')
def board_domain_testandanswer(user_domain):
    return '{} 도메인의 /board URL을 호출했습니다.'.format(user_domain)


# 5) redirect_to
#  - 특정 URL로 접근했을 때 다른 URL로 처리를 넘길 때 사용
#  - 이와 같은 이유로 redirect_to 옵션이 지정된 URL은 이전의 예제와 달리ㅣ 웹 브라우저에 HTTP 메시지의 헤더만 전달된다.

# - redirect_to 옵션을 사용하여 원래의 뷰 함수에게 처리를 맡기지 않고 다른 URL로 처리 넘기기
#  - 웹 브라우저에서 /board URL로 접근하면 강제적으로 /new_board URL이 접근되면서 웹 브라우저는 new_board() 함수가 실행된다.
@app.route('/board', redirect_to='/new_board')
def board():
    return '/board URL을 호출했는 데 실행이 안 될 겁니다.'


@app.route('/new_board')
def new_board():
    return '/new_board URL이 호출되었습니다.'


# redirect_to 옵션은 함수를 전달하는 방법도 사용된다.

# - redirect_to 옵션에 함수를 전달할 경우 함수는 미리 선언되어 있어야 한다.
# - 이 함수는 필수 인자로 URL 어댑터(adapter)를 받아야 한다.
# - 그리고 특정 URL이 URL 변수를 받을 경우 URL 변수 만큼의 이름이 동일한 인자들(id, id2)을 받아야 한다.
def redirect_new_board(adapter, id, id2):
    return '/new_board/{0}/{1}'.format(id, id2)


@app.route('/board/<id>/<id2>', redirect_to=redirect_new_board)
def board(id, id2):
    return '호출 안되는 부분'


@app.route('/new_board/<id>/<id2>')
def new_board(id, id2):
    return '{0}, {1} 변수와 함께 new_board URL이 호출되었습니다.'.format(id, id2)


# - redirect_to 옵션을 사용하여 라우팅을 지정할 때의 좋은 점
#  - 웹사이트가 개편되었을 때 이전 방문자의 링크를 안정적으로 유지할 수 있음
#  - 또 다른 뷰 함수와 before_request 데코레이터 등을 사용하지 않아도 구현할 수 있음


# 6) alias
#  - alias 옵션을 endpoint 옵션의 다른 옵션명으로 동작함
#  - 일반적으로 alias 옵션을 따로 지정하지 않고 endpoint 속성으로 사용한다.

if __name__ == '__main__':
    app.run()
