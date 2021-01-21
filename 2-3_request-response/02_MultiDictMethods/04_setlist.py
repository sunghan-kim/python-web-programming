# setlist 메서드

# setlist 메서드는 같은 이름을 가진 키 이름으로 서로 다른 값을 여러 번 전달하려고 할 때 사용한다.
# getlist 메서드와 반대되는 메서드가 setlist 메서드이다.

from werkzeug.datastructures import MultiDict

post = MultiDict()

# setlist 메서드를 사용해서 question 변수가 두 개 있고 서로 다른 값을 가지는 변수를 MultiDict에 정의한다.
post.setlist('question', ['answer1', 'answer2'])

print(post)