from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
load_dotenv()
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title = "대한민국 헌법 RAG",
    page_icon = "📚"
)

st.title("📚 대한민국 헌법 RAG 챗봇")
st.caption("대한민국 헌법 문서를 검색하여 질문에 답합니다.")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

def make_retriever() :
    with open("data/대한민국헌법.txt", "r", encoding = "utf-8") as f :
        texts = f.read()

    spltr = CharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 30,
        separator = "\n\n"
    )
    docs = spltr.split_text(texts)

    embd = OpenAIEmbeddings(
        model = "text-embedding-3-large"
    )
    vecdb = FAISS.from_texts(
        texts = docs,
        embedding = embd
    )
    rtrv = vecdb.as_retriever()
    return rtrv

if "retriever" not in st.session_state :
    try :
        with st.spinner("헌법 문서를 분석하고 있습니다...") :
            st.session_state.retriever = make_retriever()
    except Exception as e :
        st.error(f"Retriever 생성 중 오류가 발생했습니다 : {e}")
        st.stop()

rtrv = st.session_state.retriever

rewrite_tmplt = '''
지금까지의 대화 내용과 사용자의 새로운 질문을 보고,
검색에 사용할 수 있는 독립적인 질문으로 다시 작성할 것.
이전 대화를 보지 않아도 의미를 이해할 수 있는 질문이어야 한다.
질문에 직접 답하지 말고 검색용 질문만 작성할 것.
'''

rewrite_prmpt = ChatPromptTemplate.from_messages(
    [
        ("system", rewrite_tmplt),
        MessagesPlaceholder(variable_name = "chat_history"),
        ("human", "{question}")
    ]
)

rewrite_chain = rewrite_prmpt | llm | StrOutputParser()

answer_tmplt = '''
너는 질문에 대답하는 AI 어시스턴트이다.
너의 임무는 주어진 context에서 사용자의 question에 답하는 것이다.
이전 대화 내용도 참고하여 사용자의 질문이 무엇을 가리키는지 판단할 것.
context를 사용하여 question에 답할 것.
만약 context에서 답을 찾을 수 없다면,
'주어진 정보에서 질문에 대한 답을 찾을 수 없습니다.'라고 답할 것.

# context : {context}
'''

answer_prmpt = ChatPromptTemplate.from_messages(
    [
        ("system", answer_tmplt),
        MessagesPlaceholder(variable_name = "chat_history"),
        ("human", "{question}")
    ]
)

answer_chain = answer_prmpt | llm | StrOutputParser()

def format_docs(docs) :
    return "\n\n".join(doc.page_content for doc in docs)

if "messages" not in st.session_state :
    st.session_state.messages = []

for msg in st.session_state.messages :
    with st.chat_message(msg["role"]) :
        st.write(msg["content"])

prompt = st.chat_input("대한민국 헌법에 대해 질문하세요.")

if prompt :
    chat_history = []

    for msg in st.session_state.messages :
        if msg["role"] == "user" :
            chat_history.append(HumanMessage(content = msg["content"]))
        else :
            chat_history.append(AIMessage(content = msg["content"]))

    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : prompt
        }
    )

    with st.chat_message("user") :
        st.write(prompt)

    with st.chat_message("assistant") :
        with st.spinner("헌법에서 관련 내용을 검색하고 있습니다...") :
            try :
                if chat_history :
                    search_query = rewrite_chain.invoke(
                        {
                            "chat_history" : chat_history,
                            "question" : prompt
                        }
                    )
                else :
                    search_query = prompt

                rest = rtrv.invoke(search_query)
                context = format_docs(rest)

                response = answer_chain.invoke(
                    {
                        "chat_history" : chat_history,
                        "question" : prompt,
                        "context" : context
                    }
                )
            except Exception as e :
                response = f"답변 생성 중 오류가 발생했습니다 : {e}"

        st.write(response)

    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content" : response
        }
    )

with st.sidebar :
    st.header("설정")

    if st.button("대화 내용 초기화") :
        st.session_state.messages = []
        st.rerun()