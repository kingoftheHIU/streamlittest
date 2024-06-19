import streamlit as st

st.title('⚙️생산경영 (Production Magagement)🔧')
st.subheader('➡ Optimizing Processes, Enhancing Efficiency')
st.write('')
st.write('')

st.header('1️⃣ Introduction to Production Management')
st.markdown(
'''
### 생산경영의 정의
: 생산경영은 **제품이나 서비스를 효율적이고 효과적으로 생산**하기 위해 자원을 계획하고 조직하며 통제하는 과정을 말합니다. 
이는 **생산 프로세스의 최적화**를 통해 품질을 높이고 비용을 절감하며, 고객의 요구를 충족시키는 것을 목표로 합니다.

### 왜 생산경영에 관심을 갖게 되었는지
: 제가 생산경영에 관심을 가지게 된 이유는 경영학과 2학년 재학 도중 수강했던 <경영과 의사결정>이라는 과목이 매우 흥미롭고 재미있었기 때문입니다. 
이 과목을 통해 경영 의사결정의 중요성과 그 과정에 대해 깊이 있게 이해하게 되었습니다. 
그 후 <생산과 경영>이라는 강의를 통해 본격적으로 생산경영에 대해 배우게 되었으며, 이 분야의 매력에 빠지게 되었습니다. 
이러한 이유로 **산업데이터공학과를 복수전공**하게 되었으며, 이를 통해 **진로를 구체화**할 수 있었습니다.
'''
)

st.write('')

st.header('2️⃣ Key Areas of Interest')
col_1, col_2 = st.columns([1,1])

with col_1:
  st.write('### 품질 관리 (Quality Management)')
  st.write('품질 관리는 제품이나 서비스의 품질을 유지하고 향상시키기 위한 전략과 프로세스를 포함합니다. 품질 관리 시스템의 구축과 지속적인 품질 개선을 통해 고객 만족도를 높이는 것이 목표입니다.')

with col_2:
  st.write('### 공급망 관리 (Supply Chain Management)')
  st.write('공급망 관리는 원자재부터 최종 제품이 소비자에게 도달할 때까지의 전체 공급망을 효율적으로 관리하는 것을 의미합니다. 재고 최적화, 납품 시간 준수 및 비용 절감 등이 중요한 관리 요소입니다.')

col_3, col_4 = st.columns([1,1])

with col_3:
  st.write('### 린 생산 (Lean Manufacturing)')
  st.write('린 생산은 낭비를 줄이고 가치를 최대화하는 생산 방법론입니다. 제품 생산 과정에서 발생하는 낭비를 체계적으로 분석하고 개선하여 생산성을 향상시키는 것이 목적입니다.')
  
with col_4:
  st.write('### 생산 계획 및 통제 (Production Planning and Control)')
  st.write('생산 계획 및 통제는 생산 일정을 계획하고 실행하는 과정을 포함합니다. 자원 할당, 작업 스케줄링, 생산 라인 효율화 등을 통해 생산 프로세스를 효과적으로 관리하고 제품 생산의 안정성과 품질을 유지하는 것이 목표입니다.')

st.write('')

st.header('3️⃣ Projects and Research')

st.write('### 원하는 프로젝트 선택하기')
col_5, col_6 = st.columns([1,1])

with col_5:
  check = st.checkbox('🔴 **최적해 찾기**')
  if check :
    st.write('**최적해 찾기**를 선택하셨습니다.')
    st.text('문제를 해결하기 위해 Excel의 Solver 도구를 사용하여 최적화를 수행했습니다. 목표는 장난감과 각 하위조립품 쌍의 생산률을 최대화하여 총 이익을 극대화하는 것이었습니다. 제약 조건으로는 A 유형 하위조립품의 공급 한계와 B 유형 하위조립품의 공급 한계가 있었으며, 내부 생산 비용도 고려해야 했습니다. Solver는 이러한 제약 조건과 목표를 바탕으로 최적의 생산 계획을 계산해주었습니다.')
    with col_6:
      st.image('pages/optimal1.png')
      st.write('⤷ 직접 실행한 엑셀 함수입니다.')
      
col_7, col_8 = st.columns([1,1])

with col_7:
  check = st.checkbox('🟡 **변수가 2개일 때 최적해 찾기**')
  if check :
    st.write('**변수가 2개일 때 최적해 찾기**를 선택하셨습니다.')
    st.text('문제를 해결하기 위해 Excel의 Solver 도구를 사용하여 최적화를 수행했습니다. 목표는 두 가지의 변수를 이용하여 총 비용을 최소화하는 것입니다. 기계의 가동조건(고정비-2진수)으로 인해 LP보다 IP로 푸는 것이 알맞으며, LP는 실수값을 가지기 때문에 IP보다 더 많은 범위를 가지므로 최적해가 더 작을 수 있다는 점을 이용하여 계산하였습니다.')
    with col_8:
      st.image('pages/optimal2.png')
      st.write('⤷ 직접 실행한 엑셀 함수입니다.')

col_9, col_0 = st.columns([1,1])

with col_9:
  check = st.checkbox('🟢 **생산 계획표 작성하기**')
  if check :
    st.write('**생산 계획표 작성하기**를 선택하셨습니다.')
    st.text('매달 목표 생산치와 생산할 수 있는 한계치가 다른 생산 시스템에 대한 문제였습니다. Lean 생산에 따라 그때그때 생산할 수 있도록 목표하였습니다.')
    with col_0:
      st.image('pages/plan.png')
      st.write('⤷ 직접 실행한 엑셀 함수입니다.')

st.write('')

st.markdown(
  '''
  ### 프로젝트에 사용된 도구와 기술
  💡 프로젝트에 사용된 프로그램은 **엑셀의 최적해 찾기 기능**이었습니다.
  이 기능을 활용하여 데이터를 분석하고 최적화하는 과정에서 중요한 결과를 도출할 수 있었습니다. 
  또한, **선형 계획법(Linear Programming)**을 사용하여 복잡한 문제를 분석하고 해결하는 데 기여하였습니다. 
  이러한 도구와 기술을 통해 프로젝트의 목표를 달성하는 데 중요한 역할을 하였습니다.
  ''')

st.write('')

st.markdown(
  '''
  ### 프로젝트의 결과 및 성과
  💡 프로젝트에서 열심히 노력하여 **성공에 인접한 결과물**을 얻었지만, 
  앞으로는 더욱 창의적인 방법을 배우고 시도해보지 못한 접근 방식을 도전해보고 싶습니다. 
  **새로운 기술**이나 **혁신적인 방법론**을 적용하여 **더 나은 결과를 도출**하고자 합니다. 
  이러한 도전은 제 전문성을 더욱 발전시키는 중요한 기회가 될 것입니다.
  ''')

st.write('')

st.header('4️⃣ Further Reading')

st.markdown(
  '''
 ### 추천 서적
  ''')
col_01, col_02 = st.columns([1,1])

with col_01:
