# analytics-bot

A natural language analytics bot that converts plain English questions into SQL queries and runs them on viewership data.

This project was built as part of the **STAGE OTT – Analyst Intern Assignment**.

---

## 🚀 What This App Does

- Accepts analytics questions in plain English  
- Uses an LLM to generate **SQLite SQL queries**
- Executes queries on viewership data
- Displays:
  - Generated SQL
  - Query results in a table
  - Optional bar chart for grouped results
 
## 🛠️ Tech Stack

- **Frontend / UI**: Streamlit  
- **Backend Logic**: Python  
- **Database**: SQLite  
- **LLM**: GPT (via OpenRouter / OpenAI-compatible API)  
- **Data Handling**: Pandas  

Example:
Input: Total watch time for Haryanvi content
Output: SQL + aggregated result
