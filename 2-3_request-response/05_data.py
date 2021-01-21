# request.data 속성
#  - data 속성은 웹 브라우저가 보내온 데이터가 해석되지 않은 채로 저장되어 있다.
#  - Flask는 웹 브라우저가 보낸 HTTP 메시지 바디의 MIME Type(application/x-www-form-urlencoded, application/json)을 인식해
#    MultiDict 타입으로 쉽게 참조할 수 있도록 한다.
#  - 하지만 MultiDict 타입으로 해석되기 전의 데이터와 Flask가 처리 불가능한 MIME Type의 데이터는 임의적인 처리를 위해서
#    해석되지 않은 데이터를 참조하려고 할 때 data 속성이 사용된다.
#  - 즉, "Flask가 MultiDict 으로 인식하기 전의 원본 상태의 데이터를 참조하고자 할 때 data 속성이 사용되는 것"이다.
#  - 그러나 이 속성을 직접적으로 이용하기보다 get_data 메서드를 사용할 것을 권장한다.
