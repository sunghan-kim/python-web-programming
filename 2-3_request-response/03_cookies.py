# request.cookies 속성
#  - cookies 속성은 클라이언트 식별을 위한 쿠키가 저장되어 있다.
#  - 이 속성의 데이터 타입은 파이썬 딕셔너리이다.

from flask import Flask, request, redirect, make_response

app = Flask(__name__)

@app.route('/example/cookie')
def example_cookie():
    print('cookies : ', request.cookies)
    return ''

@app.route('/example/cookie_set')
def example_cookie_set():
    redirect_to_cookie = redirect('/example/cookie')
    response = make_response(redirect_to_cookie)
    # set_cookie() : 쿠키 설정
    response.set_cookie('Cookie Register', value='Example Cookie')
    return response

if __name__ == '__main__':
    app.run()
