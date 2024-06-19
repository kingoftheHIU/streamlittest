import streamlit as st

st.title('「 ✦ SUYEON HONG ✦ 」')
st.subheader(' ➡ Welcome to personal page of Suyeon! ')

st.write('')
st.write('')

st.header('1️⃣ Introduction')
col_1, col_2= st.columns([1,1])

with col_1 :
    st.write('### 학적사항')
    st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Fkr%2Ffree-icon%2Fwoman_3884857&psig=AOvVaw0-wxwZ1uD59sINSgt8Ezhs&ust=1718855837132000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCID02ZLj5oYDFQAAAAAdAAAAABAE')
    
with col_2 :
    st.write('### 전공')
    st.write('- **주전공 : 경영학과**')
    st.write('- **복수전공 : 산업데이터공학과**')
