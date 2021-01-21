# MultiDict
#  - GET과 POST 메서드로 넘어온 데이터가 (key, value)으로 된 튜플을 요소로 가지는 리스트 데이터 타입이다.
#  - 리스트 타입에서 일반적으로 제공하는 메서드가 아니라 딕셔너리 타입에서 제공하는 메서드를 제공한다.

# MultiDict 데이터 타입이 제공하는 메서드들
#  1) get
#  2) getlist
#  3) add
#  4) setlist
#  5) setdefault
#  6) setlistdefault
#  7) clear
#  8) copy
#  9) deepcopy
#  10) pop
#  11) poplist
#  12) update


# - Flask에서 request 모듈을 가져와서 사용하게 되는 args, form, values 객체에 저장되어 있는 MultiDict 데이터 타입은
#   ImmutableMultiDict 타입이다.
# - 따라서 이 데이터 타입은 객체의 내용을 수정하지 않는 get, getlist 메서드 등만 사용이 가능하고,
#   add, pop 메서드 등을 사용할 경우 예외를 발생시키게 된다.
# - 그러므로 Proxy 객체로 동작하는 flask.request 클래스에서 제공받는 args, form, values 객체에 영향을 주는 메서드 사용을
#   하지 않도록 주의해야 한다.
