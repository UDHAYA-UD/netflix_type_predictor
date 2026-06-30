import streamlit as st
import pickle
import numpy as np
import time

# ---------------- Load Model ----------------
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- Page Config ----------------
st.set_page_config(page_title="Netflix Predictor", page_icon="🎬", layout="centered")

# ---------------- Session State for Intro ----------------
if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

# ---------------- Global Netflix CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #141414;
    }

    /* Make all input text white (fixes black-on-black issue) */
    input, .stNumberInput input, .stSlider, label, .stMarkdown, p, span {
        color: #ffffff !important;
    }

    /* Slider track/thumb in Netflix red */
    .stSlider [data-baseweb="slider"] > div > div {
        background: #e50914 !important;
    }

    /* Number input box styling */
    .stNumberInput input {
        background-color: #1f1f1f !important;
        border: 1px solid #e50914 !important;
        border-radius: 4px;
    }

    /* Predict button */
    .stButton>button {
        background-color: #e50914;
        color: white !important;
        border: none;
        border-radius: 5px;
        height: 3em;
        width: 14em;
        font-weight: bold;
        font-size: 16px;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff0a16;
        transform: scale(1.05);
        box-shadow: 0 0 20px #e50914;
    }

    /* Netflix intro animation */
    @keyframes netflixZoom {
        0%   { transform: scale(0.3); opacity: 0; letter-spacing: 2px; }
        50%  { transform: scale(1.1); opacity: 1; }
        70%  { transform: scale(1.0); }
        100% { transform: scale(1.0); opacity: 1; }
    }

    .netflix-intro {
        text-align: center;
        font-size: 80px;
        font-weight: 900;
        color: #e50914;
        font-family: 'Helvetica Neue', sans-serif;
        animation: netflixZoom 2.2s ease-out forwards;
        text-shadow: 0 0 30px rgba(229,9,20,0.8);
        margin-top: 150px;
    }

    /* Title fade-in */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-15px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeIn 1.2s ease-in;
    }

    /* Result card cinematic reveal */
    @keyframes resultReveal {
        0%   { opacity: 0; transform: scale(0.7); }
        60%  { opacity: 1; transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }
    .result-card {
        animation: resultReveal 0.9s ease-out forwards;
        text-align: center;
        padding: 30px;
        border-radius: 10px;
        background: linear-gradient(145deg, #1a1a1a, #000000);
        border: 2px solid #e50914;
        box-shadow: 0 0 40px rgba(229,9,20,0.6);
        margin-top: 20px;
    }
    .result-text {
        font-size: 42px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 15px #e50914;
    }

    hr { border-color: #333; }

    /* ---- Pill-style radio buttons (replaces sliders) ---- */
    div[role="radiogroup"] {
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 6px;
        margin-bottom: 10px;
    }
    div[role="radiogroup"] label {
        background-color: #1f1f1f;
        border: 2px solid #333;
        border-radius: 20px;
        padding: 8px 18px !important;
        cursor: pointer;
        transition: all 0.25s ease;
        margin: 0 !important;
    }
    div[role="radiogroup"] label:hover {
        border-color: #e50914;
        box-shadow: 0 0 12px rgba(229,9,20,0.5);
    }
    div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
        display: none;
    }
    div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(135deg, #e50914, #b00710);
        border-color: #e50914;
        box-shadow: 0 0 18px rgba(229,9,20,0.8);
    }

    /* ---- Year stepper row ---- */
    div[data-testid="stHorizontalBlock"] {
        align-items: center !important;
        gap: 6px;
    }
    .year-display {
        text-align: center;
        font-size: 34px;
        font-weight: 800;
        color: #ffffff;
        background: #1f1f1f;
        border: 2px solid #e50914;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(229,9,20,0.4);
        letter-spacing: 2px;
        height: 2.8em;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0;
    }
    div[data-testid="column"] .stButton>button {
        width: 100%;
        height: 2.8em;
        font-size: 20px;
        background-color: #1f1f1f;
        border: 2px solid #e50914;
        margin: 0;
        padding: 0;
    }
    div[data-testid="column"] .stButton>button:hover {
        background-color: #e50914;
    }

    /* Section label styling */
    .section-label {
        color: #e50914 !important;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 4px;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Netflix Intro Sequence (with sound) ----------------
import base64
import os

def get_audio_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

if not st.session_state.intro_done:
    audio_b64 = get_audio_base64("netflix_intro.mp3")
    enter_placeholder = st.empty()

    with enter_placeholder.container():
        st.markdown(
            "<div style='text-align:center; margin-top:220px;'>"
            "<p style='color:#aaa; font-size:16px;'>Tap below for the full Netflix experience 🔊</p>"
            "</div>",
            unsafe_allow_html=True
        )
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_b:
            clicked = st.button("▶  ENTER")

    if clicked:
        enter_placeholder.empty()
        intro_placeholder = st.empty()

        if audio_b64:
            intro_placeholder.markdown(
                f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
                <div class='netflix-intro'>N</div>
                """,
                unsafe_allow_html=True
            )
        else:
            intro_placeholder.markdown(
                "<div class='netflix-intro'>N</div>",
                unsafe_allow_html=True
            )

        time.sleep(2.5)
        intro_placeholder.empty()
        st.session_state.intro_done = True
        st.rerun()
    else:
        st.stop()

# ---------------- Header ----------------
st.markdown(
    """
    <div class='fade-in'>
        <div style='text-align:center; font-size:64px; font-weight:900; color:#e50914;
                    text-shadow: 0 0 25px rgba(229,9,20,0.8); line-height:1; margin-bottom:-10px;
                    font-family: Helvetica Neue, sans-serif;'>
            N
        </div>
        <h1 style='text-align: center; color: #e50914; font-family: Helvetica Neue, sans-serif;'>
            Netflix Type Predictor
        </h1>
        <p style='text-align: center; font-size:18px; color:white;'>
            Enter details and predict whether it's a <b style="color:#e50914;">Movie</b> or a <b style="color:#e50914;">TV Show</b>
        </p>
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- User Inputs ----------------
st.subheader("📌 Enter Title Details")

# --- Release Year: custom stepper instead of number box ---
if "release_year" not in st.session_state:
    st.session_state.release_year = 2020

st.markdown("<p class='section-label'>Release Year</p>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1, 0.3, 2, 1])
with col1:
    if st.button("➖", key="year_minus"):
        st.session_state.release_year = max(1900, st.session_state.release_year - 1)
with col3:
    st.markdown(f"<div class='year-display'>{st.session_state.release_year}</div>", unsafe_allow_html=True)
with col4:
    if st.button("➕", key="year_plus"):
        st.session_state.release_year = min(2026, st.session_state.release_year + 1)

release_year = st.session_state.release_year

# --- Number of Genres: pill selector instead of slider ---
st.markdown("<p class='section-label'>Number of Genres</p>", unsafe_allow_html=True)
genre_count = st.radio(
    "genre_count", options=list(range(1, 11)), index=1,
    horizontal=True, label_visibility="collapsed"
)

# --- Title Word Count: pill selector instead of slider ---
st.markdown("<p class='section-label'>Number of Words in Title</p>", unsafe_allow_html=True)
title_word_count = st.radio(
    "title_word_count", options=list(range(1, 21)), index=2,
    horizontal=True, label_visibility="collapsed"
)

# Prepare input for model
features = np.array([[release_year, genre_count, title_word_count]])

# ---------------- Predict Button + Cinematic Reveal ----------------
if st.button("🍿 Predict"):
    loading_placeholder = st.empty()

    # Cinematic "scanning" loading effect
    loading_messages = [
        "🔍 Analyzing title pattern...",
        "🎞️ Checking genre signals...",
        "🤖 Running Random Forest model..."
    ]
    for msg in loading_messages:
        loading_placeholder.markdown(
            f"<p style='text-align:center; color:#e50914; font-size:20px;'>{msg}</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.6)

    loading_placeholder.empty()

    prediction = model.predict(features)[0]

    if prediction == "Movie":
        icon, label = "🎥", "It's a Movie!"
    else:
        icon, label = "📺", "It's a TV Show!"

    st.markdown(
        f"""
        <div class='result-card'>
            <div style='font-size:60px;'>{icon}</div>
            <div class='result-text'>{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

# ---------------- Footer ----------------
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
        Built with ❤️ using Streamlit & Random Forest — Netflix-style UI
    </p>
    """,
    unsafe_allow_html=True
)