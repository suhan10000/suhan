import streamlit as st

st.markdown("# 앱 UI 만들기")
st.markdown("---")
user_id = st.text_input("이름")
grade = st.radio("학년", ["1", "2", "3"], horizontal=True)
class = st.number_input("반", min_value=1, max_value=10, value=1)

st.select_slider("난이도", options=["쉬움", "보통", "어려움"],value="보통")
st.slider("점수")

question = st.text_area("소감", placeholder="여기에 소감을 작성해 주세요.")

st.markdown("---")

if st.button("확인"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
       {user_id}/{grade}/{class}/{난의도}
