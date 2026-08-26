import streamlit as st

# 🌟 1. 화려한 페이지 설정 🌟
st.set_page_config(page_title="MBTI 진로 탐험대", page_icon="🧭", layout="centered")

# 🎈 2. 메인 타이틀 및 소개 🎈
st.title("✨ 🧭 MBTI 맞춤형 진로 탐험대 🚀 ✨")
st.subheader("나의 성격 유형에 딱 맞는 직업은 무엇일까요? 🤔💭")
st.divider() # 예쁜 구분선

# 🌈 3. MBTI별 추천 직업 데이터 (이모지 폭발!) 🌈
mbti_jobs = {
    "INTJ": "🔬 과학자, 💻 소프트웨어 개발자, ♟️ 전략 기획자",
    "INTP": "🧠 철학자, 📐 건축가, 📊 데이터 분석가",
    "ENTJ": "👔 경영자, ⚖️ 변호사, 📈 경영 컨설턴트",
    "ENTP": "💡 발명가, 🎬 영화 감독, 🚀 창업가",
    "INFJ": "🕊️ 상담사, ✍️ 작가, 🎨 예술 감독",
    "INFP": "💖 심리 치료사, 📚 시인, 🎭 애니메이터",
    "ENFJ": "🎓 교사, 🤝 PR 전문가, 🗣️ 동기부여 연설가",
    "ENFP": "🎉 이벤트 플래너, 🎤 엔터테이너, ✈️ 여행 가이드",
    "ISTJ": "👮 경찰관, 💼 회계사, 🏥 의사",
    "ISFJ": "🩺 간호사, 🏫 초등학교 교사, 📚 사서",
    "ESTJ": "🏢 프로젝트 매니저, 🏦 은행원, ⚖️ 판사",
    "ESFJ": "🏨 호텔 지배인, 🦷 치과의사, 🤝 사회복지사",
    "ISTP": "🔧 기계 공학자, ✈️ 조종사, 💻 시스템 분석가",
    "ISFP": "🎨 화가, 👗 패션 디자이너, 🍳 셰프",
    "ESTP": "🚒 소방관, 💼 영업 사원, 🏆 스포츠 코치",
    "ESFP": "🎭 배우, 👗 패션 모델, 🥳 파티 플래너"
}

# 🎯 4. 사용자 입력 🎯
st.write("### 👇 당신의 MBTI를 선택해주세요! 👇")
mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("MBTI 16가지 유형 중 하나를 고르세요! 💖", mbti_types, index=None, placeholder="여기를 클릭하세요! 👆")

# 🎁 5. 결과 출력 (화려한 애니메이션 포함) 🎁
if selected_mbti:
    st.balloons() # 🎉 결과를 볼 때 풍선이 날아오릅니다!
    st.write("---")
    st.success(f"## 🎉 {selected_mbti} 유형을 위한 추천 진로 🎉")
    st.info(f"### {mbti_jobs[selected_mbti]}")
    st.warning("💡 **꿀팁:** 이것은 참고용일 뿐, 여러분의 가능성은 우주만큼 무궁무진합니다! 🌌✨")
