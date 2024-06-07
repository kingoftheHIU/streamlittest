import streamlit as st

st.title('타이틀 텍스트')

st.write('#1. Markdown 텍스트 작성하기')

st.markdown(
    '''
    #마크다운 헤더1
    -마크다운 목록1. **굵게**표시
    -마크다운 목록2. *기울임*표시
        -목록 2-1
        -목록 2-2
    
    ##마크다운 헤더2
    - [네이버](http://naver.com)

    ###마크다운 헤더3
    마크다운
    '''
)

import pandas as pd

st.write('#2.아무거나')
df = pd.DataFrame({
    'name' : ['A','B','C'],
    'code' : [12,34,56]
})
