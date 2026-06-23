# Project B - 뉴스 요약 자동화 워크플로우 구축

## 1. 프로젝트 개요

본 프로젝트는 RSS 피드를 활용하여 최신 AI 뉴스를 자동 수집하고, 생성형 AI를 통해 기사를 요약한 뒤 Notion 데이터베이스에 자동 저장하는 뉴스 요약 자동화 시스템을 구축하는 것을 목표로 한다.

## 2. 사용 도구

- Make
- RSS Feed
- Make AI Toolkit
- Notion
- Retry / Incomplete Execution

## 3. 최종 워크플로우 구조

Scheduler
→ RSS 뉴스 수집
→ Notion 중복 검사
→ 신규 기사 필터링
→ Array Aggregator
→ Iterator
→ 신규 기사 5건 제한
→ AI 기사 요약
→ AI 감성 분석
→ Notion 저장

## 4. 데이터 수집

RSS 피드를 통해 AI 뉴스를 자동 수집한다.

수집 데이터:
- Title
- Summary
- Description
- URL
- Author
- Date Created

## 5. 중복 방지

URL 기반 중복 검사 수행

조건:
Total Number Of Bundles = 0

## 6. 신규 기사 5건 제한

Array Aggregator + Iterator 사용

필터:
Bundle Order Position <= 5

## 7. AI 기사 요약

Make AI Toolkit 사용

프롬프트:

다음 뉴스를 한국어로 3줄 이내로 요약해줘.

제목:
{{Title}}

내용:
{{Summary}}

규칙:
- 핵심 내용만 작성
- 3줄 이내
- 추측 금지

## 8. 감성 분석

출력값:
- Positive
- Neutral
- Negative

## 9. Notion 저장

저장 속성:
- Title
- Summary
- URL
- PublishedDate
- Sentiment

## 10. 예외 처리

Retry Automatically = Yes
Number Of Retries = 2

실패
→ 재시도 1회
→ 실패
→ 재시도 2회
→ 실패
→ 최종 실패

Store Incomplete Executions = Yes

최종 실패 시 Make가 실패 로그를 저장한다.

## 11. 비용 최적화

- 중복 기사 제거
- 신규 기사 5건 제한
- RSS Summary 활용
- Retry 최대 2회 제한

## 12. 요구사항 충족

- RSS 뉴스 수집 완료
- 자동 실행 완료
- AI 기사 요약 완료
- Notion 저장 완료
- URL 저장 완료
- 발행일 저장 완료
- 중복 방지 완료
- 신규 기사 필터링 완료
- 재시도 최대 2회 완료
- 오류 로그 저장 완료
- 감성 분석 완료

## 13. 프로젝트 결과

RSS 뉴스 수집 → AI 요약 → 감성 분석 → Notion 저장까지의 전체 자동화 파이프라인을 구축하였다.

또한 URL 기반 중복 방지, 신규 기사 5건 제한, 재시도 정책, 실패 로그 저장 기능을 적용하여 안정적인 자동화 시스템을 구현하였다.
