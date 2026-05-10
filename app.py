import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Happy Mother's Day, Mommy Cherylann!",
    page_icon="🌸",
    layout="wide"
)

# ========== STYLING: BLUE SHINING WITH STARS ==========
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b3d91, #1e90ff, #87cefa);
        background-attachment: fixed;
    }
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        background-image: radial-gradient(white 1.5px, transparent 1.5px);
        background-size: 40px 40px;
        opacity: 0.4;
        animation: moveStars 60s linear infinite;
    }
    @keyframes moveStars {
        from { background-position: 0 0; }
        to { background-position: 100px 100px; }
    }
    .card-container {
        position: relative;
        z-index: 2;
        max-width: 1200px;
        margin: 2rem auto;
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        border-radius: 2rem;
        padding: 2rem;
        box-shadow: 0 0 30px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #fff9c4;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffaa00;
        text-align: center;
        margin-bottom: 1rem;
    }
    .heart {
        font-size: 2rem;
        animation: heartbeat 1s infinite;
        text-align: center;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .names-list {
        color: #fff9c4;
        font-size: 1rem;
        line-height: 1.6;
        list-style: none;
        padding-left: 0;
    }
    .names-list li {
        margin-bottom: 0.3rem;
    }
    .right-header {
        color: #ffd700;
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-heart {
        text-align: center;
        margin-top: 1rem;
    }
    audio {
        display: none;
    }
    </style>
    <div class="stars"></div>
    """,
    unsafe_allow_html=True,
)

# ---------- TWO COLUMN LAYOUT: PHOTO LEFT, NAMES RIGHT ----------
col_left, col_right = st.columns([1, 1])

with col_left:
    image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/cherylenn.jpeg"
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="💖 Mommy Cherylann 💖", width=350)
    except Exception as e:
        st.error(f"Could not load the image.\n\n{str(e)}")

with col_right:
    st.markdown('<div class="right-header">📍 From Brit\'s Home Grand Goave Haiti</div>', unsafe_allow_html=True)
    names = [
        "Sandiana Septembre", "Daffecat Michel", "Sophonia Darius", "Marie Prisca Rodney",
        "Volmar Lovena", "Daya Joachim", "Horlinne François", "Shelove Polisca",
        "Isselande Miselin", "Nashca Pierre", "Pierre Louis Guerlanda", "Djoudemie Jean Baptiste",
        "Isemylove Galioth", "Christie Paul", "Valentina Etienne", "Dapheka Jeanlubin",
        "Daphené Jeanlubin", "Soriya Mérisme", "Rose Mania François", "Anie François",
        "Dieuna Robert", "Woodshaina Bolivar", "Bedsaida Louis", "Solaika", "Djemaya"
    ]
    # Split into two columns for better fit
    half = len(names) // 2
    col_names1, col_names2 = st.columns(2)
    with col_names1:
        for name in names[:half]:
            st.markdown(f'<div class="names-list">💖 {name}</div>', unsafe_allow_html=True)
    with col_names2:
        for name in names[half:]:
            st.markdown(f'<div class="names-list">💖 {name}</div>', unsafe_allow_html=True)

# ---------- MESSAGE BELOW THE TWO COLUMNS ----------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🌸 Happy Mother's Day, Mommy Cherylann! 🌸</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1.2rem; color:white; text-align:center;">We love you and celebrate you today!</p>
        <div class="sub-heart">💐 With love from all of us 💐</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- BACKGROUND MUSIC (hidden) ----------
audio_html = """
<audio id="bgMusic" autoplay loop style="display:none;">
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>
<script>
    var audio = document.getElementById('bgMusic');
    audio.volume = 0.5;
    audio.play().catch(e => console.log("Autoplay prevented."));
</script>
"""
st.markdown(audio_html, unsafe_allow_html=True)
st.caption("🎵 Background music playing (if allowed by browser)")
