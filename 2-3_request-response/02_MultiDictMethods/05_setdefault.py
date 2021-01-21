# setdefault 메서드

# add 메서드와 하는 일이 유사하다.
# add 메서드와의 차이점은 설정하고자 하는 변수가 없을때에만 default 값으로 데이터를 추가하고,
# 설정하고자 하는 변수가 있으면 변수값을 반환한다.

from werkzeug.datastructures import MultiDict

# 기본값으로 변수 설정하기 (단, 기존 변수가 선언되어 있지 않은 경우)
post = MultiDict()
post.add('foo', 'ham')
post.setdefault('foo', 'ham2')
post.setdefault('lorem', 'answer')

print(post)