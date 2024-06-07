import streamlit as st

st.title('「 ✦ SUYEON HONG ✦ 」')

st.write(' ➡ 본 웹페이지는 홍수연의 비전과 앞으로의 계획에 대해 소개하는 페이지 입니다.')

st.header('✔️사이드바')
st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

st.header('## 1️⃣ 개인정보')
col_1, col_2, col_3 = st.columns([1:1:1])

with col_1 :
    st.write('### 학적사항')
    st.check

st.markdown(
    '''
    ### I 개인정보🧬
    - 1. **전공** 
        - 1-1 주전공 : 경영학과
        - 1-2 복수전공 : 산업데이터공학과
    - 2. **교내 활동** 
        - 2-1 중앙동아리 터사랑 부회장
        - 2-2 총동아리연합회 레저분과장
    - 3. **학적 사항**
        - 3-1 학년 : 3학년 (22학년도 입학)

    ### II 앞으로의 비전🎓
    - 1. **복수전공을 한 이유**
        ➤ 경영학과 세부전공은 총 7가지 (참고자료 : [홍익대학교 홈페이지](https://bizadmin.hongik.ac.kr/dept/biz/0303.html))
            이 중 생산경영을 세부전공으로 선택하기로 결정
            ❔ '경영과 의사결정'이라는 과목과 '생산과 경영'이라는 강의에 흥미를 느낌
           
    ### III 준비 과정
    일반 텍스트
    '''
    )
