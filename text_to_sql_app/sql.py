from dotenv import load_dotenv
load_dotenv() # load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])

    return response.text

# Function to retrieve query from the database

def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English to SQL code!
    The SQL database has the name STUDENT and has the following columns = NAME, CLASS, SECTION
    \n\nFor example, 
    \nExample 1 - How many entries of records are present ?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me students who study in machine learning class?, 
    the SQL command will be something like this SELECT * FREOM STUDENT where CLASS="Machine Learning";
    also the sql code should not have ''' in the beginning or end and sql word is output
    """
]

# Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrive SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked 

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in response:
        st.header(row)

