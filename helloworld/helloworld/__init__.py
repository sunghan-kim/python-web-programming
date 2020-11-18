# Flask Skeleton Program

from flask import Flask

# flask 객체 생성
# flask 객체는 웹 브라우저로 오는 모든 요청과 템플릿과의 연계 등 웹 애플리케이션 전반에 대해서 영향을 끼치는 메인 객체이다.
# Flask 클래스는 모듈의 이름을 인자로 받음
#  - __name__ : 실행 중인 모듈의 이름을 가리키는 변수
#  - 프로그래머가 임의로 제공할 때는 임의 문자열도 전달할 수 있다.
app = Flask(__name__)

# URL "/"의 GET 요청에 대해 뷰 함수를 등록
#  - 뷰 함수의 등록은 뷰 함수로 이용되는 함수의 선언 위에 Flask 인스턴스인 app 객체 변수의 route 데코레이터를 사용함
#  - route 데코레이터는 첫 번째 인자를 반드시 필요로 함 (나머지 인자는 옵션으로 제공)
@app.route("/")
def helloworld():
    # 뷰 함수는 처리가 끝나면 반드시 클라이언트에 응답을 반환하기 위해 return 문을 사용
    return "Hello World"