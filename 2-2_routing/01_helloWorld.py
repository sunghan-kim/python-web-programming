from flask import Flask

app = Flask(__name__)


# route 데코레이터는 route 함수가 처리할 HTTP 메서드 타입을 한 개 이상 지정할 수 있음
@app.route('/')
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()

# 뷰 함수 : route 데코레이터가 추가된 함수

#