# update 메서드

# update 메서드는 기존의 MultiDict 타입 변수에 다른 MultiDict 타입 변수의 내용을 삽입하는 데 사용한다.
# 파이썬 딕셔너리에서의 update와 같은 일을 한다.

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add('foo', 'ham')
print('post before : ', post)

get = MultiDict()
get.add('lorem', 'issue')

post.update(get)

print('post after : ', post)
