# AI Agent · 데이터 자동화 포트폴리오

현실의 문제를 정의하고, 필요한 데이터와 업무 흐름을 구조화한 뒤 **AI·데이터·자동화 기술을 선택해 구현하고 검증한 학습·응용 산출물**을 정리한 공개용 저장소입니다.

> 이 저장소는 교육과정 실습, 응용 실습, 진행 중 프로젝트를 구분합니다. 수업 산출물을 독립적인 상용 프로젝트로 주장하지 않습니다.

## 핵심 방향

`문제정의 → 구조화 → 방법 선택 → 프로토타입/구현 → 검증 → 개선`

- **Code & Data**: Python, pandas, SQL, API/JSON
- **AI & Agent**: LangChain, LangGraph, RAG, Vector DB, Tool Calling, Dify
- **Automation & No/Low-code**: Make, Zapier, Dify Workflow
- **Service & Visualization**: Streamlit, Tableau
- **교육과정 실습 경험**: Graph DB / Neo4j (별도 보존 산출물 없음)
- **현재 경험으로 주장하지 않는 영역**: RDF, RDFS, OWL, Ontology 설계

## 프로젝트/실습 구성

| 폴더 | 내용 | 분류 |
|---|---|---|
| `01_constitution_rag` | 대한민국 헌법 기반 RAG 챗봇 / 대화형 RAG | 수업·확장 실습 |
| `02_langgraph_agent` | LangGraph 상태·분기·Tool Calling | 수업 실습 |
| `03_make_zapier_automation` | 댓글 모니터링 Workflow 자동화 | 응용 실습 / 대표 자동화 사례 |
| `04_dify_workflows` | Dify Workflow / Chatflow / Agent export | 수업 실습 |
| `05_tableau` | Tableau 시각화 Workbook | 수업 실습 |
| `06_sql` | JOIN·집계·CTE·LAG·CASE | 수업 실습 |
| `07_python_applications` | Mastermind / 두음 변환 응용 | 응용 실습 |
| `08_final_project` | 서울 상권 분기별 지표 비교 자동화 | 진행 중 |

## 보안 및 공개 범위

공개 저장소용 사본에서는 다음을 제거하거나 치환했습니다.

- `.env`, API key, 인증 토큰, 개인 이메일/연결정보
- `__pycache__`, 로컬 가상환경, 로컬 Vector DB
- 개인정보가 포함될 수 있는 Gmail/Google Sheets 캡처와 원본 보고서
- 공개 권한이 불분명하거나 실행에 필수적이지 않은 원자료

`.env.example`을 복사해 로컬 `.env`를 만들고 필요한 키를 직접 입력하세요. **실제 `.env`는 Git에 커밋하지 마세요.**

## 참고

일부 파일은 원래 교육 환경에서 생성된 산출물의 **공개용 정리본**입니다. 로컬 파일경로와 인증정보가 제거되어 원본과 1:1로 실행되지 않을 수 있으며, 각 폴더 README에 필요한 조건을 적었습니다.
