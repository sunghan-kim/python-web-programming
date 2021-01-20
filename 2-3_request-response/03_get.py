# 1. get 메서드

# 1.1 기본값
# 웹 브라우저로부터 특정 변수가 전달되지 않았을 때 특정 값을 이 변수의 기본값으로 설정할 수 있다.
# Flask는 다른 프레임워크에 비해 더 간단히 기본값을 설정할 수 있다.

# 웹 브라우저로부터 특정 변수가 넘어오지 않았을 때 기본값 반환하기
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/board", methods=["GET", "POST"])
def board():
    # question 변수가 브라우저로부터 전달되지 않았을 경우 question 변수를 MultiDict에서 가져오더라도 오류가 발생하지 않고
    # "질문을 입력하십시오"라는 값을 반환하게 된다.
    # 기본값으로 가져올 값은 get 메서드를 사용할 때
    #  - default 인자명 생략 시 -> 두 번째 위치에 넣어 줌
    #  - 인자명을 사용해 전달 시 -> default 인자명과 함께 기본값을 전달
    return request.values.get("question", "질문을 입력하십시오")


# 1.2 기본 타입

# 일반적인 언어에서 특정 변수를 숫자 타입으로 변환할 때의 로직
#  1) 웹 브라우저가 보낸 데이터를 특정 변수에 저장
#  2) 특정 변수를 숫자 타입으로 변환한 다음, 특정 변수에 덮어씀

# Flask 에서는 get 메서드의 세 번째 옵션으로 type 인자를 제공한다.
# type 인자를 사용하면 특정 변숫값을 특정 데이터 타입으로 만들어서 쉽게 사용할 수 있다.

# get 메서드에 type 인자에 변환 타입 제공
@app.route("/board2", methods=["GET", "POST"])
def board2():
    # type=int : answer 변수값을 받아올 떄 int 객체로 반환
    return str(request.values.get("answer", 1, type=int))


# type 옵션의 값으로 사용 가능한 값
#  1) 파이썬에서 기본적으로 제공하는 데이터 타입
#  2) 사용자 데이터 타입 (함수 또는 호출 가능한 클래스의 인스턴스를 넘김)

# Y-m-d 타입으로 넘어온 데이터를 datetime 형태로 반환하는 사용자 데이터 타입 (함수형)
def dateKoreanType(date_format):
    def translate(date_str):
        return datetime.strptime(date_str, date_format)
    return translate

# 중첩 함수 (내포 함수)
#  - 특정 함수를 사용자 데이터 타입 변환에 사용하려면 함수는 타입을 변환할 데이터 하나만 인자로 받아야 한다.
#  - 그런데 데이터 해석에 필요한 함수가 해석할 날짜 타입과 같은 옵션 인자를 받아야 하는 경우가 있다.
#  - 이 때, 데이터 해석에 필요한 함수는 실제 데이터 해석을 하는 함수를 반환해야 한다.
#  - 이렇게 작성되는 함수를 "중첩 함수" 또는 함수가 다른 함수 안에 포함되어 있다는 의미로 "내포 함수"로 부르기도 한다.


@app.route('/board3', methods=['GET', 'POSE'])
def board3():
    print(request.values.get('date', '2015-02-09', type=dateKoreanType("%Y-%m-%d")))
    return '날짜는 콘솔을 확인해보세요.'


# 만약 임의의 목적으로 쓰기 위해 정의한 사용자 정의 타입이 클래스로 구현되어 있다면, MultiDict의 get 메서드에서 사용하기 위해
# 호출 메서드인 "__call__" 메서드를 정의 하기만 하면 된다.
class dateKoreanType2:
    def __init__(self, format):
        self.format = format

    # __call__ 메서드는 self 인자 외에 가변 인자(*args), 키워드 가변 인자(**kwargs)를 인자로 선언해야 한다.
    # Flask가 변환하라고 전달하는 날짜는 가변 인자(*args)의 첫 번째 값으로 전달받는다.
    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)


@app.route('/board4', methods=['GET', 'POST'])
def board4():
    print(request.values.get('date', '2015-02-09', type=dateKoreanType2('%Y-%m-%d')))
    return '날짜는 콘솔을 확인해보세요.'


if __name__ == "__main__":
    app.run(host="127.0.0.1")
