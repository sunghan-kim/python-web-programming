# request.blueprint 속성
#  - blueprint 속성은 특정 URL이 어떤 Blueprint에 속해 있는 지 알고 싶을 때 사용한다.
#  - 특정 URL이 어떠한 Blueprint에도 속하지 않을 경우의 속성값은 "None" 이다.

from flask import Flask, request, Blueprint

app = Flask(__name__)

bp = Blueprint('bp', __name__)

@bp.route('/example/blueprint', methods=['GET', 'POST'])
def example_environ():
    print(request.blueprint)
    return ''

app.register_blueprint(bp)
app.run()


