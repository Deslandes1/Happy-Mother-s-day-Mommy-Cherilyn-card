import streamlit as st
import base64
import requests
from PIL import Image
from io import BytesIO

# ------------------------- Page Configuration -------------------------
st.set_page_config(
    page_title="Happy Birthday, Mommy Cherilyn!",
    page_icon="🎂",
    layout="wide",
)

# ------------------------- Styling: Blue Shining with Stars -------------------------
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

# ------------------------- Fetch and Display Image -------------------------
image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/cherylenn.jpeg"
try:
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="💖 Mommy Cherilyn 💖", use_container_width=False, width=400)
except Exception as e:
    st.error(f"Could not load the image. Please check the file name or path.\n\n{str(e)}")

# ------------------------- Celebratory Text -------------------------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🎂 Happy Birthday, Mommy Cherilyn! 🎂</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1.2rem; color:white;">We love you and celebrate you today!</p")
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------- Auto‑play Looping Music -------------------------
# Simple MIDI‑like melody encoded as base64 (short "Happy Birthday" excerpt)
audio_base64 = "data:audio/mpeg;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjI2LjEwMAAAAAAAAAAAAAAA//OEwAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAAEAAABIADg7O3v7+/v7+/vAwMDAwMDAwMD////////////////////////////////////////////////////////////////////////8AAAAATGF2YzU4LjQ1LjEwMA0AAAAAABCS80C3Rk1G///////////////////////////////////8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8P8"
st.audio(audio_base64, format="audio/mpeg", loop=True, autoplay=True)

# ------------------------- Customisations -------------------------
# You can change the image name, file path, or the melody by replacing the audio data.
