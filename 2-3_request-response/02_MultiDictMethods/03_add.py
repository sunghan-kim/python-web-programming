# add 메서드

# add 메서드는 MultiDict에 키와 값을 추가하는 메서드이다.
# 일반적으로 사용되는 메서드는 아니지만, 웹 브라우저가 보내온 데이터를 기준으로 MultiDict에 키와 값을 추가할 수 있다.

from werkzeug.datastructures import MultiDict

# add 메서드를 사용해 MultiDict 데이터 타입에 키와 값 추가하기
post = MultiDict()
post.add('question', 'answer')

print(post)

# add 메서드는 키와 값이 일대일로 매치되어 있는 경우 유용하게 사용할 수 있다.
