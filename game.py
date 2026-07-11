import streamlit as st

st.title("counter app")
if 'count' not in st.session_state:
   st.session_state.count = 0 
 
if st.button("증가"):
   st.session_state.count += 1
st.markdown(f"## 현재 숫자: `{st.session_state.count}`")
