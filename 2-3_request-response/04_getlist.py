# getlist 메서드

# getlist 메서드는 get 메서드와 달리 이름은 같고 값이 다른 데이터들을 리스트 타입으로 반환한다.
# 이런 예는 중복 체크(ex. 관심 분야 선택)를 하는 곳에서 쉽게 찾아볼 수 있다.


from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


class dateKoreanType:
    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)


# getlist 메서드를 사용해서 같은 이름을 가진 데이터를 리스트 타입으로 가져오기
@app.route('/board', methods=['GET', 'POSTS'])
def board():
    print(request.values.getlist('dates', type=dateKoreanType('%Y-%m-%d')))
    return '날짜들은 콘솔을 확인해보세요.'

# getlist 메서드는 get 메서드와 달리 defaults 인자를 받지 않는다.
# 그 이유는 변숫값이 넘어오지 않은 경우 기본값으로 빈 리스트를 반환하기 때문이다.


if __name__ == "__main__":
    app.run(host="127.0.0.1")

