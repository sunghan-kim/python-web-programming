# 라우팅 지정 (routing Designation)

from flask import Flask

app = Flask(__name__)


# Flask에서 웹 애플리케이션의 라우팅 지정 방법
#  - route 데코레이터 사용
#  - add_url_rule 메서드 사용

# 1. route 데코레이터 사용
#  - 뷰 함수로 등록하고자 하는 함수를 route 데코레이터로 데코레이팅하는 것으로 끝낼 수 있다.
#  - route 데코레이터에 두 번째 인자를 전달할 때 인자 이름을 포함해 전달하지 않으면, route 데코레이터는 두 번째 인자를
#    endpoint 인자로 인식한다.
@app.route("/flask")
def index():
    return ''


# 2. add_url_rule 메서드 사용
#  - 뷰 함수를 미리 만들어 놓고 라우팅 지정을 하려 할 때 사용
#  - add_url_rule 메서드는 인자 이름과 값을 지정하지 않으면 인자를 넘긴 순서대로 다음 객체들로 인식한다.
#    - 처리할 URL
#    - 뷰 함수의 별칭(alias)
#    - 뷰 함수 객체
#  - 그리고 route 데코레이터와 같은 방식으로 추가 인자를 키워드 방식으로 지정한다.
def index():
    return ''


app.add_url_rule('/', 'index', index)

# - add_url_rule 메서드는 대규모 애플리케이션 제작 시에 특정 라우팅을 뺴고 싶을 때 유용하게 사용할 수 있다.
#   (route 데코레이터와 add_url_rule 메서드 : 관리의 차이)
