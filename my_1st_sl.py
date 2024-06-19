import streamlit as st

st.title('「 ✦ SUYEON HONG ✦ 」')
st.subheader(' ➡ Welcome to personal page of Suyeon! ')

st.write('')
st.write('')

st.header('1️⃣ Introduction')
col_1, col_2= st.columns([1,1])

with col_1 :
    st.write('### 학적사항')
    st.image('C:\Users\hsy11\Downloads\free-icon-woman-6785697.png')
    
with col_2 :
    st.write('### 전공')
    st.write('- **주전공 : 경영학과**')
    st.write('- **복수전공 : 산업데이터공학과**')
