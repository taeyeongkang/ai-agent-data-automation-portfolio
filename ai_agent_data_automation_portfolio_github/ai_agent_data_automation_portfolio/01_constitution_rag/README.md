# 대한민국 헌법 RAG Chatbot

대한민국 헌법 텍스트를 분할하고 OpenAI Embeddings + FAISS로 검색한 뒤, 검색 결과를 LLM에 전달하는 RAG 실습입니다.

- 기본 버전: `app.py`
- 대화 이력을 이용해 검색질문을 재작성하는 확장 버전: `conversational_rag.py`
- Vector DB 생성: `create_db.py`

## 실행 예시

```bash
pip install -r ../requirements.txt
cp ../.env.example ../.env
streamlit run app.py
```

`OPENAI_API_KEY`를 로컬 `.env`에 입력해야 합니다.

> 분류: 수업/확장 실습. 운영 서비스 경험이나 정량적 검색 정확도 개선 성과를 주장하지 않습니다.
