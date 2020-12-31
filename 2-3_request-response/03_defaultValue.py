# 기본값

# 웹 브라우저로부터 특정 변수가 전달되지 않았을 때 특정 값을 이 변수의 기본값으로 설정할 수 있다.
# Flask는 다른 프레임워크에 비해 더 간단히 기본값을 설정할 수 있다.

# 웹 브라우저로부터 특정 변수가 넘어오지 않았을 때 기본값 반환하기
from flask import Flask, request

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("question", "질문을 입력하십시오")

if __name__ == "__main__":
    app.run(host="127.0.0.1")