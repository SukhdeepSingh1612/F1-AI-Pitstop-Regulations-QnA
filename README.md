# Formula 1 Regulations Q&A

A Streamlit web app that lets you ask questions about Formula 1 regulations using LangChain, Astra DB (Cassandra), and OpenAI embeddings & LLMs. The app searches the Astra DB vector store to find relevant F1 rulebook snippets and answers your queries interactively.

---

## Features

- Natural language Q&A about Formula 1 rules.
- Semantic search on regulations stored in Astra DB (Cassandra).
- Uses OpenAI embeddings to vectorize queries and documents.
- Provides relevant rule snippets along with answers.
- Clean, Ferrari-themed UI built with Streamlit.

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Astra DB (Cassandra)
- OpenAI API
- Dotenv (for environment variable management)

---

## Setup & Installation

1. Clone this repository or copy the code locally.

2. Install dependencies:
    ```bash
    pip install streamlit python-dotenv langchain cassio openai
    ```

3. Create a `.env` file in the root directory and add the following:
    ```
    ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
    ASTRA_DB_ID=your_astra_database_id
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    Replace `app.py` with the filename if different.

---

## Usage

- Open the Streamlit app in your browser.
- Enter your question about F1 regulations in the input box.
- Press "Ask" to get the answer and related regulation snippets.
- Expand the snippets section to read relevant rule excerpts.

---

## Notes

- Make sure your Astra DB is properly set up with the relevant vector store table (`qa_mini_demo`).
- This app requires valid API keys for both OpenAI and Astra DB.
- The UI is styled with a Formula 1 / Ferrari theme.

---

## License

MIT License © Sukhdeep Singh

---

## Contact

Built with ❤️ by Sukhdeep Singh

Feel free to reach out for questions or collaborations.
