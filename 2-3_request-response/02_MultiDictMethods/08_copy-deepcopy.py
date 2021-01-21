# copy, deepcopy 메서드

# copy 메서드와 deepcopy 메서드는 MultiDict 데이터 타입 변수에 저장된 모든 값을 복사한다.
#  - copy 메서드
#   - MultiDict 데이터 타입의 복사에 있어 변숫값으로 리스트 타입이 있는 경우 해당 리스트 타입의 메모리 주소를 복사
#   - 얕은 복사
#  - deepcopy 메서드
#   - 리스트 타입의 메모리 주소가 아닌 데이터를 복사
#   - 깊은 복사

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add('foo', ['ham', 'ham2'])
print('post : ', post)

post_copy = post.copy()
post_deepcopy = post.deepcopy()

post_copy['foo'].extend(['ham3'])
post_deepcopy['foo'].extend(['ham4'])

# post_copy는 얕은 복사를 하기 때문에 post 변수의 foo 변수값이 변경된 것을 확인할 수 있다.
# post_deepcopy는 깊은 복사를 하기 때문에 post에 저장된 foo 변수에 영향을 받지 않게 된다.

print('post : ', post)
print('post_copy : ', post_copy)
print('post_deepcopy : ', post_deepcopy)
