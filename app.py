import streamlit as st

# -----------------------------------------
# 화면 설정
# -----------------------------------------

st.set_page_config(
    page_title="태양계 몸무게 계산기",
    page_icon="🪐",
    layout="centered"
)


# -----------------------------------------
# 글씨 크게 설정
# -----------------------------------------

st.markdown("""
<style>
.큰제목 {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
}

.설명 {
    font-size: 22px;
    text-align: center;
    line-height: 1.8;
    margin-bottom: 30px;
}

.stSelectbox label {
    font-size: 24px !important;
    font-weight: bold !important;
}

.stSelectbox div {
    font-size: 22px !important;
}

.stNumberInput label {
    font-size: 24px !important;
    font-weight: bold !important;
}

.stNumberInput input {
    font-size: 24px !important;
    padding: 15px !important;
}

.stButton button {
    font-size: 26px !important;
    font-weight: bold !important;
    padding: 15px !important;
    width: 100%;
}

.결과제목 {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
    margin-top: 40px;
}

.결과숫자 {
    font-size: 64px;
    font-weight: bold;
    text-align: center;
    margin: 20px 0 30px 0;
}

.안내 {
    font-size: 25px;
    font-weight: bold;
    text-align: center;
    line-height: 1.8;
    margin-top: 30px;
}

.설명2 {
    font-size: 20px;
    text-align: center;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# 제목
# -----------------------------------------

st.markdown(
    '<div class="큰제목">🪐 태양계 몸무게 계산기</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="설명">다른 행성과 달에서는 내 몸무게가<br>얼마나 되는지 알아보세요.</div>',
    unsafe_allow_html=True
)


# -----------------------------------------
# 천체의 중력 비율
# 지구의 중력을 1로 기준
# -----------------------------------------

천체중력 = {
    "태양": 27.010,
    "수성": 0.378,
    "금성": 0.907,
    "지구": 1.000,
    "달": 0.165,
    "화성": 0.377,
    "목성": 2.360,
    "토성": 0.916,
    "천왕성": 0.889,
    "해왕성": 1.120
}


# -----------------------------------------
# 천체 선택
# -----------------------------------------

선택한천체 = st.selectbox(
    "태양계 행성 선택",
    list(천체중력.keys())
)


# -----------------------------------------
# 몸무게 입력
# -----------------------------------------

몸무게 = st.number_input(
    "나의 몸무게",
    min_value=0.0,
    value=0.0,
    step=0.1,
    format="%.1f"
)


# -----------------------------------------
# 계산하기 버튼
# -----------------------------------------

if st.button("계산하기"):

    # 몸무게가 0인 경우
    if 몸무게 == 0:

        st.markdown(
            '<div class="안내">몸무게를 1kg 이상 입력해 주세요.</div>',
            unsafe_allow_html=True
        )

    else:

        # -----------------------------------------
        # 선택한 천체에서의 몸무게 계산
        # -----------------------------------------

        중력비율 = 천체중력[선택한천체]

        계산된몸무게 = 몸무게 * 중력비율

        # 소수점 한 자리까지 반올림
        계산된몸무게 = round(계산된몸무게, 1)

        # 천 단위 쉼표와 소수점 한 자리 표시
        결과 = f"{계산된몸무게:,.1f}kg"


        # -----------------------------------------
        # 결과 표시
        # -----------------------------------------

        st.markdown(
            f'<div class="결과제목">{선택한천체}에서의 몸무게</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="결과숫자">{결과}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div class="설명2">
            지구에서 {몸무게:,.1f}kg인 경우<br>
            {선택한천체}의 중력을 기준으로 계산한 값입니다.
            </div>
            ''',
            unsafe_allow_html=True
        )

