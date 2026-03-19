import streamlit as st
import get_csv_data

stbk = get_csv_data.extrato_bancario().all_statement()

st.title("Finance Control")

for statement in stbk:
    st.dataframe(statement)