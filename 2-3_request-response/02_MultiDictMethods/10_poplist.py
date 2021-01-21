# poplist 메서드

# poplist 메서드는 pop 메서드와 같은 일을 하지만 같은 이름의 변수 키로 여러 값이 들어올 때 이를 꺼내오기 위해 사용한다.
# getlist 메서드와 유사한 동작을 하지만, 꺼내온 뒤에는 MultiDict 변수에서 해당 변수 키를 찾아볼 수 없다.

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist('foo', ['ham', 'ham2'])
print('post before : ', post)

foo_values = post.poplist('foo')
print('post after : ', post)

if 'foo' not in post:
    print('post 변수에 더 이상 foo 변수가 없습니다.')

