import streamlit as st

st.title('「 ✦ SUYEON HONG ✦ 」')
st.subheader(' ➡ 본 웹페이지는 홍수연의 비전과 앞으로의 계획에 대해 소개하는 페이지 입니다.')

st.write('')
st.write('')

st.sidebar.write('### ✔️사이드바')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

st.header('1️⃣ 개인정보')
col_1, col_2, col_3 = st.columns([1,1,1])

with col_1 :
    st.write('### 학적사항')
    st.write('- 3학년')
    st.write('- 22학년도 입학')
    
with col_2 :
    st.write('### 전공')
    st.write('- **주전공 : 경영학과**')
    st.write('- **복수전공 : 산업데이터공학과**')

with col_3 : 
    st.write('### 교내활동')
    st.write('- 중앙동아리 터사랑 부회장')
    st.write('- 총동아리연합회 레저분과장')
    
st.write('')

st.header('2️⃣ 앞으로의 비전')

st.write('### 1. 복수전공을 한 이유')
st.write(' ➤ 경영학과 세부전공은 총 7가지 (참고자료 : [홍익대학교 홈페이지](https://bizadmin.hongik.ac.kr/dept/biz/0303.html))')
st.write('**생산경영**을 세부전공으로 선택하기로 결정')
st.write('생산경영을 깊이 공부하기 위해선 데이터 공부가 필수적, 이후 학과 커리큘럼을 보며 산업데이터공학에 대해 복수전공 결정')

st.write('### 2. 생산경영이란?')
