import streamlit as st

st.title("counter app")
count = 0 
if st.button("증가"):
   count += 1
   st.markdown(f"## 현재 숫자: `{count}`")
