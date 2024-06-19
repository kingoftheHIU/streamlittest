import streamlit as st


st.title('「 ✦ SUYEON HONG ✦ 」')
st.subheader(' ➡ Welcome to personal page of Suyeon! ')

st.write('')
st.write('')

st.header('1️⃣ Introduction')
col_1, col_2= st.columns([1,1])

with col_1 :
    st.image('girl.png')
   
with col_2 :
    st.write('### Who am I?')
    st.write('안녕하세요! 😊 저는 홍수연(Suyeon Hong)입니다. 항상 웃음을 잃지 않고 주변에 긍정 에너지를 전파하는 것이 제 특기랍니다! 🌟 새로운 도전과 배움을 사랑하며, 사람들과의 소통을 즐기는 외향적인 성격을 가지고 있어요. 생산경영에 대한 열정으로 매일 조금씩 성장해 나가는 중이에요. ')

st.header('2️⃣ Personal Information')
st.markdown(
    '''
    - **이름(Name)** : 홍수연
    - **생년월일(Birthdate)** : 2003.06.15
    - **연락처(Contact Information)** : 10-4030-1169
    - **이메일(Email Address)** : hsy1169@naver.com
    - **주소(Adress)** : 경기도 광명시 하안동
   '''
   )
st.header('3️⃣ About Me')
tab_1, tab_2, tab_3, tab_4 = st.tabs(['학력(Educational Background)', '경력(Professional Background)', '기술(Skills)', '취미와 관심사(Hobbies and Interests)'])

with tab_1:
    st.write('### 학력(Educational Background)')
    st.markdown(
    '''
    - 홍익대학교 경영학전공 입학 (22.03)
    - 홍익대학교 산업데이터공학 복수전공 (24.03)
   '''
   )

with tab_2:
    st.write('### 경력(Professional Background)')
    st.markdown(
    '''
    - 홍익대학교 경영학전공 CD분반 집행부원 (23.03)
    - 홍익대학교 총동아리연합회 레저분과장 (24.03)
    - 홍익대학교 중앙동아리 터사랑 부회장 (24.03)
   '''
   )
    
with tab_3:
    st.write('### 기술(Skills)')
    st.markdown(
    '''
    - 컴퓨터활용능력 1급
    - 품질경영기사 (따고 싶음)
    - 토익 xxx점
    - 토플 xxx점
   '''
   )

with tab_4:
    st.write('### 취미와 관심사(Hobbies and Interests)')
    st.markdown(
    '''
    - 여행
   '''
   )
    st.image('travel1.jpg')
    st.image('travel2.jpg')
    st.image('travel3.jpg')
