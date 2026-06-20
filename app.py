import streamlit as st

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------------------------
# CSS
# -----------------------------------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#172554,#1e3a8a);
}

/* HERO CARD */

.hero{
padding:90px 60px;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,0.1);
border-radius:30px;
text-align:center;
animation:fadeIn 1.2s ease;
}

.hero h1{
color:white;
font-size:70px;
font-weight:700;
margin-bottom:20px;
}

.hero p{
font-size:22px;
color:#cbd5e1;
line-height:1.8;
}

/* FEATURE CARDS */

.feature{
padding:30px;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(15px);
border-radius:25px;
transition:0.4s;
text-align:center;
color:white;
height:220px;
}

.feature:hover{
transform:translateY(-12px);
box-shadow:0px 15px 35px rgba(56,189,248,.35);
}

.feature h2{
margin-top:20px;
font-size:24px;
}

.feature p{
margin-top:15px;
color:#d1d5db;
}

/* ACCURACY CARD */

.accuracy{
padding:40px;
background:rgba(255,255,255,.08);
border-radius:25px;
text-align:center;
color:white;
}

.accuracy h1{
font-size:65px;
color:#38bdf8;
}

@keyframes fadeIn{
from{
opacity:0;
transform:translateY(30px);
}

to{
opacity:1;
transform:translateY(0px);
}
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HERO SECTION
# -----------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🎓 Student Performance Predictor</h1>

<p>
Predict mathematics scores using Machine Learning and intelligent analytics.
Built with modern AI techniques for fast and accurate predictions.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------
# BUTTON
# -----------------------------------------------------

c1, c2, c3 = st.columns([2,1,2])

with c2:
    if st.button("🚀 Get Started", use_container_width=True):
        st.switch_page("pages/1_Predict.py")

st.write("")
st.write("")
st.write("")

# -----------------------------------------------------
# FEATURES
# -----------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">

    <h1>📈</h1>

    <h2>ML Prediction</h2>

    <p>
    Advanced machine learning models deliver accurate score prediction.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">

    <h1>⚡</h1>

    <h2>Real-Time Results</h2>

    <p>
    Generate predictions instantly with optimized preprocessing pipelines.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">

    <h1>🎯</h1>

    <h2>High Accuracy</h2>

    <p>
    Trained models provide reliable predictions with excellent performance.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# -----------------------------------------------------
# MODEL ACCURACY
# -----------------------------------------------------

st.markdown("""
<div class="accuracy">

<h1>90%</h1>

<h3>Model Accuracy</h3>

</div>
""", unsafe_allow_html=True)