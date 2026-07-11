import streamlit as st

st.markdown("# 앱 UI 만들기")
name = st.text_input("이름", placeholder = "이름")
grade = st.radio("학년",["1", "2", "3"], horizontal = True)
class_num = st.number_input("반", min_value=1, max_value=10, value=1)
difficulty = st.select_slider("난이도",options=["매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"],value="보통")
score = st.slider("점수", 0, 100, 50)
text = st.text_area("소감입니다.")

if st.button("확인"):
    st.success(f"{name} / {grade}학년 / {class_num} / {difficulty}")
    st.markdown(f"점수: {score, color : green}")
    st.info(f"소감: {text}")
    
        
    
