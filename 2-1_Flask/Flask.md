# 1. Flask 클래스

## 1.1 Flask 인스턴스화

- `app = Flask(__name__)`
- 위 방법 외에도 여러 인자를 주어 Flask 애플리케이션 개발에서 실행 환경의 일부 옵션을 쉽게 변경할 수 있다.

## 1.2 Flask 클래스 인스턴스화에 자주 사용되는 인자들

```python
Flask(import_name, static_url_path, static_folder, template_folder)
```

### 1.2.1 `import_name`

- 애플리케이션 패키지의 이름을 지정하는 인자
- 문자열 값으로 정의
- 보통은 `__name__` 변수를 넘겨서 애플리케이션 이름을 생성
- `Flask` 클래스로부터 인스턴스를 생성할 때 꼭 필요한 인자

### 1.2.2 `static_url_path`

- 정적 파일(CSS, 이미지 등)을 서비스하는 `static_folder` 폴더를 웹에서 접근할 때 어떤 경로를 사용할 것 인지 지정
- 이 인자는 문자열 값으로 정의
- `/` 문자로 시작할 수 없음
- 정의하지 않으면 기본값으로 `static` 사용

### 1.2.3 `static_folder`

- 프로그램 소스 트리에서 정적 파일(CSS, 이미지 등)을 서비스하는 폴더명을 지정
- 이 인자는 문자열 값으로 정의
- 정의하지 않으면 기본값으로 `static` 사용

### 1.2.4 `template_folder`

- 프로그램 소스 트리에서 뷰 함수가 사용할 HTML 파일이 위치하는 폴더명을 지정
- 이 인자는 문자열 값으로 정의
- 정의하지 않으면 기본값으로 `templates`를 사용

## 1.3 Flask 객체 변수로부터 할 수 있는 작업들

- Flask 클래스로부터 객체 생성이 완료되면, app 변수는 Flask 인스턴스를 담고 있는 객체 변수(인스턴스)로 취급된다.
- Flask는 객체 변수로부터 다음 작업을 할 수 있다.

1. 글로벌 객체 (`globalObject.py`)
2. 사용자 응답 객체 생성 (`userResponseObject.py`)
3. HTTP 요청 전후에 대한 핸들러 관리 (`handlerManagement.py`)
4. 사용자 정의 URL 처리 함수 관리 (`userDefinedUrlManagement.py`)
5. 미들웨어 등록을 위한 순수 WSGI 객체 접근 (`WSGIObjectAccess.py`)
6. 디버그 모드 설정 (`setDebugMode.py`)