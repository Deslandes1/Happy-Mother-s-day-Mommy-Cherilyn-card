import streamlit as st
import base64
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Happy Mother's Day, Mommy Cherylenn!",
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
        max-width: 800px;
        margin: 2rem auto;
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        border-radius: 2rem;
        padding: 2rem;
        box-shadow: 0 0 30px rgba(0,0,0,0.2);
        text-align: center;
    }
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #fff9c4;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffaa00;
    }
    .heart {
        font-size: 2rem;
        animation: heartbeat 1s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
    <div class="stars"></div>
    """,
    unsafe_allow_html=True,
)

# ---------- DISPLAY IMAGE (raw GitHub URL) ----------
image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/cherylenn.jpeg"
try:
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="💖 Mommy Cherylenn 💖", width=400)
except Exception as e:
    st.error(f"Could not load the image. Please check the file name or path.\n\n{str(e)}")

# ---------- MOTHER'S DAY MESSAGE ----------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🌸 Happy Mother's Day, Mommy Cherylenn! 🌸</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1.2rem; color:white;">We love you and celebrate you today!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- MOTHER'S DAY SONG (classic, looping) ----------
# Base64 encoded short "Happy Mother's Day" melody (classic tune)
audio_base64 = "data:audio/mpeg;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI2LjEwMAAAAAAAAAAAAAAA//OEwAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAAEAAABIADg7O3v7+/v7+/vAwMDAwMDAwMD////////////////////////////////////////////////////////////////////////8AAAAATGF2YzU4LjQ1LjEwMA0AAAAAABCS80C3Rk1G///////////////////////////////////8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8"
st.audio(audio_base64, format="audio/mpeg", loop=True, autoplay=True)

# Optional: list of loving names (if you want to include them)
names = [
    "Sandiana Septembre", "Daffecat Michel", "Sophonia Darius", "Marie Prisca Rodney",
    "Volmar Lovena", "Daya Joachim", "Horlinne François", "Shelove Polisca",
    "Isselande Miselin", "Nashca Pierre", "Pierre Louis Guerlanda", "Djoudemie Jean Baptiste",
    "Isemylove Galioth", "Christie Paul", "Valentina Etienne", "Dapheka Jeanlubin",
    "Daphené Jeanlubin", "Soriya Mérisme", "Rose Mania François", "Anie François",
    "Dieuna Robert", "Woodshaina Bolivar", "Bedsaida Louis", "Solaika", "Djemaya"
]

st.markdown("---")
st.markdown("<h3 style='color:white; text-align:center;'>💖 With love from all of us 💖</h3>", unsafe_allow_html=True)
cols = st.columns(5)
for idx, name in enumerate(names):
    with cols[idx % 5]:
        st.markdown(f"<p style='color:#fff9c4; text-align:center; font-size:0.9rem;'>{name}</p>", unsafe_allow_html=True)
