# MenuMind

냉장고에 있는 재료를 입력하면 AI가 사용자의 조건에 맞는 요리를 추천해주는 웹 서비스입니다.

## 1. 서비스 소개

MenuMind는 집에 있는 식재료를 어떻게 활용할지 고민하는 사용자를 위한 AI 요리 추천 서비스입니다.

사용자가 가지고 있는 재료와 원하는 요리 난이도, 조리 시간을 입력하면 AI가 조건에 맞는 요리를 추천하고 필요한 재료와 조리 방법을 알려줍니다.

## 2. 주요 기능

- 냉장고에 있는 재료 입력
- 요리 난이도 선택
- 원하는 조리 시간 선택
- AI를 활용한 요리 추천
- 예상 조리 시간 안내
- 필요한 재료 안내
- 단계별 조리 방법 제공
- 입력값이 없을 경우 안내 메시지 표시
- API 요청 실패 시 오류 메시지 표시
- 모바일 화면을 고려한 반응형 웹 디자인

## 3. 페이지 구성

MenuMind는 하나의 웹페이지 안에서 다음 3개의 섹션으로 구성되어 있습니다.

### 홈
- 서비스 소개
- AI 요리 추천 화면으로 이동

### AI 요리 추천
- 보유 재료 입력
- 요리 난이도 선택
- 조리 시간 선택
- AI 추천 결과 확인

### 이용방법
- 재료 입력
- 조건 선택
- AI 추천의 3단계 사용 방법 안내

상단 내비게이션을 통해 각 섹션으로 이동할 수 있습니다.

## 4. 사용 기술

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Vercel Serverless Function

### AI
- Codyssey Public API
- OpenAI 호환 Chat Completions API
- GPT-5 Mini

### Deployment
- GitHub
- Vercel

## 5. 프로젝트 구조

```text
menumind/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── app.js
├── api/
│   └── recommend.py
├── images/
├── requirements.txt
├── README.md
├── SERVICE_PLAN.md
├── .gitignore
└── vercel.json
```

## 6. AI 요청 및 응답 흐름

사용자가 웹페이지에서 재료와 조건을 입력하면 JavaScript의 `fetch()`를 이용해 `/api/recommend`로 데이터를 전송합니다.

Python Serverless Function은 전달받은 데이터를 이용해 프롬프트를 만들고 Codyssey의 OpenAI 호환 API에 요청합니다.

AI가 생성한 요리 추천 결과를 서버가 JSON 형태로 프론트엔드에 반환하고 JavaScript가 결과를 화면에 표시합니다.

```text
사용자 입력
    ↓
JavaScript fetch()
    ↓
/api/recommend
    ↓
Python Serverless Function
    ↓
Codyssey AI API
    ↓
GPT-5 Mini
    ↓
JSON 응답
    ↓
웹페이지 결과 출력
```

## 7. 예외 처리

다음 상황에 대한 예외 처리를 구현했습니다.

- 재료를 입력하지 않은 경우 입력 안내 메시지 표시
- AI API 요청 중 버튼을 비활성화하고 로딩 상태 표시
- API 또는 서버 오류 발생 시 사용자에게 오류 메시지 표시

## 8. 환경 변수

AI API 키는 코드에 직접 작성하지 않고 Vercel Environment Variables를 통해 관리합니다.

```text
OPENAI_API_KEY
```

API 키의 실제 값은 보안을 위해 GitHub 저장소에 포함하지 않습니다.

## 9. 로컬 실행 방법

별도의 프론트엔드 프레임워크를 사용하지 않았기 때문에 `index.html`을 VS Code의 Live Server로 실행하여 화면을 확인할 수 있습니다.

로컬 Live Server에서는 Vercel Serverless Function이 실행되지 않으므로 AI API 기능은 배포된 Vercel 환경에서 확인합니다.

## 10. 배포 방법

GitHub 저장소와 Vercel을 연결하여 배포했습니다.

Vercel의 Root Directory는 다음과 같이 설정했습니다.

```text
A1-3/menumind
```

GitHub의 `main` 브랜치에 코드를 Push하면 Vercel에서 자동으로 새로운 버전을 배포합니다.

배포 환경에서는 정적 프론트엔드와 `/api/recommend` Python Serverless Function이 함께 동작합니다.

## 11. 배포 URL

MenuMind Vercel 배포 주소:

```text
https://la-codyssey.vercel.app
```

## 12. 개발 과정에서 학습한 내용

이번 프로젝트를 통해 HTML은 웹페이지의 구조, CSS는 화면의 디자인과 반응형 구성, JavaScript는 사용자 입력 처리와 API 통신을 담당한다는 것을 학습했습니다.

또한 JavaScript의 `fetch()`를 사용하여 프론트엔드에서 서버로 요청을 보내고 JSON 응답을 받아 화면에 표시하는 과정을 직접 구현했습니다.

Python 기반 Vercel Serverless Function을 이용하여 AI API 키가 브라우저에 노출되지 않도록 서버에서 AI API를 호출하도록 구성했습니다.

또한 로컬 환경과 Vercel 배포 환경의 차이를 확인하고 Vercel의 Build Logs와 Runtime Logs를 이용하여 배포 오류와 API 호출 오류를 확인하고 해결하는 방법을 학습했습니다.