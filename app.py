import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Happy Birthday, Sebastien Stephane Deslandes!",
    page_icon="🎂",
    layout="wide"
)

# Compact styling to fit in one screenshot
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #6b0f1a, #b22222, #ffb347, #ffd700);
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
        background-image: radial-gradient(#ffd700 1.5px, transparent 1.5px);
        background-size: 40px 40px;
        opacity: 0.3;
        animation: moveStars 60s linear infinite;
    }
    @keyframes moveStars {
        from { background-position: 0 0; }
        to { background-position: 100px 100px; }
    }
    .card-container {
        position: relative;
        z-index: 2;
        max-width: 1100px;
        margin: 0.5rem auto;
        background-color: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(8px);
        border-radius: 1.5rem;
        padding: 0.8rem;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    .title {
        font-size: 2.2rem;
        font-weight: bold;
        color: #fff9c4;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffaa00;
        text-align: center;
        margin: 0 0 0.2rem 0;
    }
    .heart {
        font-size: 1.5rem;
        animation: heartbeat 1s infinite;
        text-align: center;
        margin: 0;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .names-list {
        color: #fff9c4;
        font-size: 0.9rem;
        line-height: 1.3;
        list-style: none;
        padding-left: 0;
        margin: 0;
    }
    .names-list li {
        margin-bottom: 0.2rem;
    }
    .right-header {
        color: #ffd700;
        font-size: 1.1rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.3rem;
        text-shadow: 0 0 5px #b22222;
    }
    .sub-heart {
        text-align: center;
        margin-top: 0.2rem;
    }
    /* Reduce bottom padding of Streamlit columns */
    .stColumn {
        padding: 0 !important;
    }
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0;
    }
    audio {
        display: none;
    }
    </style>
    <div class="stars"></div>
    """,
    unsafe_allow_html=True,
)

# ---------- TWO‑COLUMN LAYOUT WITH REDUCED SPACING ----------
col_left, col_right = st.columns([1, 1], gap="small")

with col_left:
    image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/Sebastien%20Stephane%20Deslandes.jpg"
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img = img.rotate(-90, expand=True)  # adjust as needed
        st.image(img, caption="🎉 Sebastien Stephane Deslandes 🎉", width=280, use_container_width=False)
    except Exception as e:
        st.error(f"Could not load image.\n{str(e)}")

with col_right:
    st.markdown('<div class="right-header">🎂 From Deslandes Family<br>we wish you a <b>Happy Birthday!</b> 🎂</div>', unsafe_allow_html=True)
    signers = ["Gesner Deslandes", "Gesner Junior Deslandes", "Roosevelt Deslandes", "Zendaya Christelle Deslandes"]
    st.markdown('<ul class="names-list">', unsafe_allow_html=True)
    for name in signers:
        st.markdown(f'<li>💖 {name}</li>', unsafe_allow_html=True)
    st.markdown('</ul>', unsafe_allow_html=True)

# ---------- MESSAGE BELOW (compact) ----------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🎂 Happy Birthday, Sebastien! 🎂</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1rem; color:white; text-align:center; margin:0;">May your day be filled with joy, strength, and love.</p>
        <div class="sub-heart">💐 With love from all of us 💐</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- HIDDEN MUSIC ----------
audio_html = """
<audio id="bgMusic" autoplay loop style="display:none;">
    <source src="https://www.kozco.com/tech/LRMonoPhase4.wav" type="audio/wav">
</audio>
<script>
    var audio = document.getElementById('bgMusic');
    audio.volume = 0.3;
    audio.play().catch(e => console.log("Autoplay blocked"));
    document.body.addEventListener('click', function() { audio.play(); });
</script>
"""
st.markdown(audio_html, unsafe_allow_html=True)
