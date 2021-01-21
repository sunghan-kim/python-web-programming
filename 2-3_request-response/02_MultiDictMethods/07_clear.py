# clear 메서드

# clear 메서드는 MultiDict 타입에 생성된 모든 값을 제거한다.

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist('foo', ['ham', 'ham2'])
print(post)

post.setlistdefault('foo2', ['answer', 'answer2'])
print(post)

post.clear()
print(post)
