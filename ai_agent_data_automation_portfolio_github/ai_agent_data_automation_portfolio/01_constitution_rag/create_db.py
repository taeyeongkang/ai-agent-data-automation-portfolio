from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_txt_vectordb() : 
    with open("data/대한민국헌법.txt", "r", encoding="utf-8") as f : 
        texts = f.read()

    spltr = CharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        separator = "\n\n"
    )

    docs = spltr.split_text(texts)
    embd = OpenAIEmbeddings(model="text-embedding-3-large")
    vecdb = FAISS.from_texts(texts=docs, embedding=embd)
    return vecdb