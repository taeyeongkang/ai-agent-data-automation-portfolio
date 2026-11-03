# 댓글 모니터링 자동화 — Python × Make × Zapier

반복적인 댓글 모니터링 업무를 데이터 처리와 Workflow 자동화로 연결한 응용 실습입니다.

## 문제와 흐름

1. Python으로 댓글 데이터 정제
2. Make에서 Gmail 첨부 CSV 수신·파싱
3. Google Sheets에 전체댓글/주의댓글 적재
4. 주의댓글을 별도로 분류
5. Zapier에서 담당자 검토 요청
6. 일정 시간 후 해당 댓글 상태를 재조회
7. 여전히 `미확인`인 경우에만 리마인드

원본 실행 기록에서는 **전처리 175건, 주의댓글 50건**을 확인했고, Zapier는 9 Step으로 구성했습니다.

## 공개 파일

- `python_preprocess_and_email_clean.ipynb`: 개인 이메일 제거 및 output 정리본
- `make_blueprint_sanitized.json`: Gmail connection / Spreadsheet ID 등 연결정보 제거본

## 공개 저장소에서 제외한 원본

개인정보와 연결식별자가 포함될 수 있어 개발보고서 DOCX/PPTX, Gmail 캡처, Google Sheets 실행결과, Zapier 화면 캡처는 공개용 ZIP에서 제외했습니다. 면접/비공개 포트폴리오에서는 별도 제시할 수 있습니다.

> 분류: 응용 실습. 실제 운영 조직에 배포된 상용 시스템으로 주장하지 않습니다.
