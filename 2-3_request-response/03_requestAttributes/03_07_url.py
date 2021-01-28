# request 속성 중 현재 URL 정보를 참조하기 위해 사용하는 여러 속성들
#  - request 속성 중에는 웹 브라우저가 처리를 요청한 라우팅 주소(URL)에 대해 여러 표현 방법으로 반환하는 속성들이 있다.
#    - path, script_root, base_url, url, url_root

#  - ex) URL : http://www.example.com/myapplication?x=y
#    - path : /myapplication
#    - script_root : 없음
#    - base_url : http://www.example.com/myapplication
#    - url : http://www.example.com/myapplication?x=y
#    - url_root : http://www.example.com/

# - 해당 속성들은 템플릿에서 유용하게 사용할 수 있다.

from flask import Flask, request

app = Flask(__name__)

@app.route('/example/environ', methods=['GET', 'POST'])
def example_environ():
    return (
        'path: %s<br>'
        'script_root: %s<br>'
        'url: %s<br>'
        'base_url: %s<br>'
        'url_root: %s<br>'
    ) % (
        request.path,
        request.script_root,
        request.url,
        request.base_url,
        request.url_root
    )

app.run()
