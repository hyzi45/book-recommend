import streamlit as st

st.title("도서 추천 서비스")
user_input = st.text_input("당신의 이름을 입력하세요:")
st.write(f"{user_input} 님을 위한 추천 도서 리스트입니다.")
