import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Prediction Result",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# CHECK SESSION
# ---------------------------------------------------
if "predicted_score" not in st.session_state:
    st.warning("Please predict first.")
    st.stop()

score = float(st.session_state.predicted_score)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#172554,#1e3a8a);
}

/* RESULT CARD */

.result-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(20px);
padding:60px;
border-radius:30px;
text-align:center;
color:white;
border:1px solid rgba(255,255,255,.1);
}

/* SUBJECT CARD */

.subject-card{
background:rgba(255,255,255,.08);
padding:35px;
border-radius:25px;
text-align:center;
color:white;
transition:.4s;
}

.subject-card:hover{
transform:translateY(-10px);
box-shadow:0px 10px 30px rgba(56,189,248,.35);
}

/* PERFORMANCE CARD */

.performance-card{
background:rgba(255,255,255,.08);
padding:40px;
border-radius:25px;
color:white;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
f"""
<div class="result-card">

<h1>🎯 Predicted Mathematics Score</h1>

<h1 style="font-size:90px;color:#38bdf8;">
{score:.2f}
</h1>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------------------------------------------
# PROGRESS BAR
# ---------------------------------------------------
st.subheader("Performance Level")

st.progress(min(int(score),100))

# ---------------------------------------------------
# PERFORMANCE MESSAGE
# ---------------------------------------------------
if score >= 80:
    performance = "🌟 Excellent Performance"

elif score >= 60:
    performance = "✅ Good Performance"

elif score >= 40:
    performance = "⚠ Average Performance"

else:
    performance = "❌ Needs Improvement"

st.markdown(
f"""
<div class="performance-card">

<h2>{performance}</h2>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------------------------------------------
# SUBJECT SUMMARY
# ---------------------------------------------------
st.subheader("Subject Summary")

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown(
    f"""
    <div class="subject-card">

    <h2>📖 Reading</h2>

    <h1>{st.session_state.reading_score}</h1>

    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    f"""
    <div class="subject-card">

    <h2>✍ Writing</h2>

    <h1>{st.session_state.writing_score}</h1>

    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    f"""
    <div class="subject-card">

    <h2>🧮 Mathematics</h2>

    <h1>{score:.2f}</h1>

    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.write("")

# ---------------------------------------------------
# PREDICT AGAIN
# ---------------------------------------------------
c1,c2,c3 = st.columns([1,2,1])

with c2:

    if st.button(
        "🔄 Predict Again",
        use_container_width=True
    ):
        st.switch_page("pages/1_Predict.py")