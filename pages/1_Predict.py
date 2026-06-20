import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Prediction Dashboard",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#172554,#1e3a8a);
}

/* TITLE */

.title{
text-align:center;
padding:20px;
color:white;
}

.title h1{
font-size:55px;
}

.title p{
font-size:18px;
color:#cbd5e1;
}

/* FORM CARD */

.form-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(20px);
padding:40px;
border-radius:30px;
border:1px solid rgba(255,255,255,.1);
}

/* METRIC CARDS */

.metric-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(20px);
padding:30px;
border-radius:25px;
text-align:center;
color:white;
transition:0.4s;
}

.metric-card:hover{
transform:translateY(-8px);
box-shadow:0px 10px 25px rgba(56,189,248,.3);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="title">

<h1>📈 Prediction Dashboard</h1>

<p>
Provide student details to predict mathematics performance.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Select Gender", "male", "female"],
        index=0
    )

    race_ethnicity = st.selectbox(
        "Race Ethnicity",
        [
            "Select Race",
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ],
        index=0
    )

    parental_level_of_education = st.selectbox(
        "Parental Education",
        [
            "Select Education",
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ],
        index=0
    )

with col2:

    lunch = st.selectbox(
        "Lunch Type",
        [
            "Select Lunch",
            "standard",
            "free/reduced"
        ],
        index=0
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        [
            "Select Course",
            "none",
            "completed"
        ],
        index=0
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=None,
        placeholder="Enter Reading Score"
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=None,
        placeholder="Enter Writing Score"
    )

st.write("")
st.write("")

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

c1, c2, c3 = st.columns([1,2,1])

with c2:

    if st.button(
        "🚀 Predict Math Score",
        use_container_width=True
    ):

        if (
            gender == "Select Gender"
            or race_ethnicity == "Select Race"
            or parental_level_of_education == "Select Education"
            or lunch == "Select Lunch"
            or test_preparation_course == "Select Course"
            or reading_score is None
            or writing_score is None
        ):

            st.warning("Please fill all fields.")

        else:

            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()

            predict_pipeline = PredictPipeline()

            results = predict_pipeline.predict(pred_df)

            st.session_state.predicted_score = results[0]

            st.session_state.reading_score = reading_score

            st.session_state.writing_score = writing_score

            st.switch_page("pages/2_Result.py")

st.write("")
st.write("")
st.write("")

# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="metric-card">

    <h1>90%</h1>

    <h3>Accuracy</h3>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="metric-card">

    <h1>0.89</h1>

    <h3>R² Score</h3>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="metric-card">

    <h1>CatBoost</h1>

    <h3>Best Model</h3>

    </div>
    """, unsafe_allow_html=True)