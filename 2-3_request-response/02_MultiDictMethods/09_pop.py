# pop 메서드

# pop 메서드는 get 메서드와 유사한 일을 하지만 기능상의 차이가 있다.
#  - get 메서드 : MultiDict 데이터 변수에서 특정 변수 키의 키 값을 메모리에 복사해서 프로그램에 반환
#  - pop 메서드 : 변수 키의 키 값을 메모리에서 복사하는 것이 아닌 MultiDict 데이터 변수에서 변수 키를 제거하고 그 값을 반환

from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add('foo', 'foobar')
print('post before : ', post)

foo_value = post.pop('foo')
print('post after : ', post)

if 'foo' not in post:
    print('post 변수에 더 이상 foo 변수 키가 없습니다.')


# pop 메서드는 두 번째 인자로 꺼내오고자 하는 변수 키가 없는 경우에 대한 기본값을 지정한다.
# 두 번째 인자의 이름은 default 이다.
post2 = MultiDict()
post2.add('foo2', 'foobar2')
foo_value2 = post2.pop('foo2', default='aaa')
foo_value3 = post2.pop('foo2', default='aaa')

print('foo_value2 : ', foo_value2)
print('foo_value3 : ', foo_value3)
