# request.is_xhr 속성
#  - is_xhr 속성은 웹 브라우저가 Ajax 요청을 보냈는 지 확인하기 위해 사용하는 속성이다.
#  - HTTP 메시지 헤더에 "X-Requested-With" 가 선언되어 있을 때에만 정상적으로 동작한다.
#    - 대표적으로 jQuery, Mochikit, Prototype 등의 라이브러리가 Ajax 요청을 할 때 "X-Requested-With" 헤더 값을 보낸다.
#    - 이 헤더에 "XMLHttpRequest" 값을 설정해서 웹 어플리케이션에 보내온다.
#    - 그리고 웹 어플리케이션에 이 헤더의 값은 True로 설정되어 웹 브라우저에서 확인이 가능하다.

# - is_xhr 속성은 최근 삭제되었다.

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/environ', methods=['GET', 'POST'])
def example_environ():
    print(request.is_xhr)
    return ''

app.run()
