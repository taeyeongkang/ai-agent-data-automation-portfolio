from env.my_gpt_env import my_gpt_env_setting
import streamlit as st
from create_db import load_txt_vectordb
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="헌법 Chatbot", page_icon=":books:")
st.title("대한민국 헌법 기반 Q/A Chatbot")

llm = my_gpt_env_setting(tmp=0.0)
if not llm :
    st.error("OpenAI API Key를 사용하여 LLM 모델을 가져올 수 없습니다")
    st.stop()

vecdb = load_txt_vectordb()
rtrv = vecdb.as_retriever()
tmplt = """
너는 대한민국 헌법에 대하여 답변하는 전문가다.
Context : {context}
Question : {question}
사용자의 질문(Question)에 대하여 Context에 바탕한 답변을 하라.
1. 답변에 사용된 해당 조항이나 내용을 바탕으로 답변하라.
2. Context에서 사용자의 질문(Quesiton)에 대한 답변을 찾을 수 없다면, "질문에 대한 답을 대한민국 헌법에서는 찾을 수 없습니다."라고 답하라.
3. Context에 제시된 내용 이외에 다른 지식을 활용하여 답변하지 마라.
4. 답변에 사용된 해당 조항을 근거로 함께 제시하라.
답변 예시
답변 : (여기에 질문에 대한 답을 넣을 것)
근거 : 제1조 1항
"""

prompt = ChatPromptTemplate.from_template(tmplt)
rag_chain = (
    {"context" : rtrv, "question" : RunnablePassthrough()} | prompt | llm | StrOutputParser()
)

if "messages" in st.session_state : 
    for msg in st.session_state.messages : 
        st.chat_message(msg["role"]).write(msg["content"])
else : 
    st.session_state["messages"] = []

if user_input := st.chat_input("대한민국 헌법에 대하여 궁금한 것을 물어보세요") : 
    st.session_state.messages.append({"role" : "user", "content" : user_input})
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant") : 
        with st.spinner("대한민국 헌법 조항을 검색해서 답변을 생성하는 중입니다.") : 
            response = rag_chain.invoke(user_input)
            st.write(response)
            st.session_state.messages.append({"role" : "assistant", "content" : response})