import os
import streamlit as st
from dotenv import load_dotenv
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import cassio

# Load environment variables
load_dotenv()
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Cassandra connection
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Initialize LangChain components
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

astra_vector_store = Cassandra(
    embedding=embeddings,
    table_name="qa_mini_demo",
    session=None,
    keyspace=None
)
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# Streamlit page config
st.set_page_config(page_title="F1 Regulations Q&A", page_icon="🏁", layout="centered")

# --- F1 THEME HEADER ---
st.markdown("""
    <div style='text-align: center; padding: 1rem; background-color: #111; border-radius: 10px;'>
        <h1 style='color: #e10600;'>🏎️ Formula 1 Regulations Q&A</h1>
        <p style='color: white;'>Ask anything about the F1 rulebook</p>
    </div>
""", unsafe_allow_html=True)

# --- INPUT FORM ---
with st.form("query_form"):
    question = st.text_input("🔍 What do you want to know?", placeholder="e.g. What are the red flag rules?")
    submitted = st.form_submit_button("Ask")

# --- RESPONSE ---
if submitted and question.strip():
    with st.spinner("🏁 Racing through the regulations..."):
        try:
            answer = astra_vector_index.query(question.strip(), llm=llm).strip()
            st.markdown("### ✅ Answer")
            st.write(answer)

            with st.expander("📘 View Relevant Regulation Snippets"):
                docs = astra_vector_index.vectorstore.similarity_search_with_score(question, k=3)
                for i, (doc, score) in enumerate(docs):
                    st.markdown(f"**Snippet {i+1}** (Relevance Score: `{score:.4f}`)")
                    st.write(doc.page_content)
                    st.markdown("---")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# --- FOOTER ---
st.markdown("""
    <hr style='border: 1px solid #444;'/>
    <div style='text-align: center; color: #aaa; font-size: 0.9rem;'>
        Built with ❤️ by Sukhdeep Singh using LangChain, Astra DB & OpenAI · Styled like Ferrari 🟥🖤
    </div>
""", unsafe_allow_html=True)
