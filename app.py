import streamlit as st
import sqlite3
import pandas as pd
from openai import OpenAI
import os

# ------------------ SCHEMA ------------------
SCHEMA = """
Table: viewership
Columns:
- view_id (int)
- user_id (int)
- content_title (string)
- dialect (string: 'Haryanvi', 'Rajasthani', 'Bhojpuri')
- watch_duration_sec (int)
- device_type (string: 'Mobile', 'SmartTV', 'Web')
- timestamp (datetime)
- region (string)
"""

# ------------------ LLM CLIENT ------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# ------------------ TEXT TO SQL ------------------
def text_to_sql(question: str):
    try:
        prompt = f"""
You are a SQL expert.

Schema:
{SCHEMA}

Convert the following question into a valid SQLite SQL query.
Return ONLY the SQL query. No explanation.

Question:
{question}
"""
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw_sql = response.choices[0].message.content.strip()
        sql = raw_sql.replace("```sql", "").replace("```", "").strip()
        return sql, None

    except Exception as e:
        return None, str(e)

# ------------------ RUN SQL ------------------
def run_query(sql: str):
    try:
        conn = sqlite3.connect("stage_analytics.db")
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df, None
    except Exception as e:
        return None, str(e)

# ------------------ STREAMLIT UI ------------------
st.set_page_config(page_title="STAGE Analytics Bot")

st.title("📊 STAGE Analytics Bot")
st.caption("Ask questions about viewership data in plain English")

question = st.text_input("Ask a question:")

if question:
    sql, llm_error = text_to_sql(question)

    if llm_error:
        st.error("Failed to generate SQL. Please try again.")
        st.stop()

    with st.expander("Show generated SQL"):
        st.code(sql, language="sql")

    result, sql_error = run_query(sql)

    if sql_error:
        st.error("SQL execution failed.")
        st.stop()

    st.subheader("Result")
    st.dataframe(result)
