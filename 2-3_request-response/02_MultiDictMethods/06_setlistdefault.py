# setlistdefault 메서드

# setdefault 메서드와 하는 일이 유사하다.
# setdefault 메서드와의 차이점은 같은 이름으로 여러 변수를 설정하고자 하는 경우에 사용한다.

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist('foo', ['ham', 'ham2'])
post.setlistdefault('foo', ['answer', 'answer2'])

print(post)
