import streamlit as st

st.markdown("# 앱 UI 만들기")
st.markdown("---")
user_id = st.text_input("이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
age = st.number_input("반", min_value=1, max_value=10, value=1)

st.select_slider("난이도", options=["쉬움", "보통", "어려움"],value="보통")
st.slider("점수")

question = st.text_area("소감", placeholder="여기에 소감을 작성해 주세요.")

st.markdown("---")

if st.button("확인"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
        if age < 14:
            st.info("참고: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
    else:
        st.error("⚠️ 동의 항목에 체크해야 전송이 가능합니다.")
