import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Happy Birthday, Sebastien Stephane Deslandes!",
    page_icon="🎂",
    layout="wide"
)

# ---------- STYLING: HOPE, FORCE, EVERLASTING LOVE ----------
st.markdown(
    """
    <style>
    /* Remove default Streamlit padding */
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
    }
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
        max-width: 1200px;
        margin: 0.5rem auto;
        background-color: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 2rem;
        padding: 1rem 1.5rem;
        box-shadow: 0 0 40px rgba(0,0,0,0.3);
    }
    .title {
        font-size: 2rem;
        font-weight: bold;
        color: #fff9c4;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffaa00;
        text-align: center;
        margin: 0.2rem 0;
    }
    .heart {
        font-size: 1.8rem;
        animation: heartbeat 1s infinite;
        text-align: center;
        margin: 0.2rem 0;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .names-list {
        color: #fff9c4;
        font-size: 1.2rem;
        line-height: 1.8;
        list-style: none;
        padding-left: 0;
        margin-top: 0.5rem;
    }
    .names-list li {
        margin-bottom: 0.3rem;
    }
    .right-header {
        color: #ffd700;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 5px #b22222;
        margin: 0 0 0.5rem 0;
        line-height: 1.2;
    }
    .right-header small {
        font-size: 1.2rem;
    }
    .sub-heart {
        text-align: center;
        margin: 0.2rem 0 0 0;
    }
    audio {
        display: none;
    }
    /* Reduce image caption size */
    .stImage figcaption {
        font-size: 0.8rem;
    }
    </style>
    <div class="stars"></div>
    """,
    unsafe_allow_html=True,
)

# ---------- TWO‑COLUMN LAYOUT: PHOTO LEFT, NAMES RIGHT ----------
col_left, col_right = st.columns([1, 1.2])   # right column slightly wider

with col_left:
    image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/Sebastien%20Stephane%20Deslandes.jpg"
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        # Rotate to correct orientation (use -90 or 90)
        img = img.rotate(-90, expand=True)
        st.image(img, caption="🎉 Sebastien Stephane Deslandes 🎉", width=300)
    except Exception as e:
        st.error(f"Could not load the image.\n\n{str(e)}")

with col_right:
    # Larger greeting
    st.markdown('<div class="right-header">🎂 we wish you a<br>Happy Birthday! 🎂</div>', unsafe_allow_html=True)
    # Names with bigger hearts
    signers = ["Gesner Deslandes", "Gesner Junior Deslandes", "Roosevelt Deslandes", "Zendaya Christelle Deslandes"]
    for name in signers:
        st.markdown(f'<p class="names-list" style="font-size:1.3rem;">💖 {name}</p>', unsafe_allow_html=True)

# ---------- COMPACT MESSAGE BELOW ----------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🎂 Happy Birthday, Sebastien! 🎂</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1rem; color:white; text-align:center; margin:0.2rem 0;">May your day be filled with joy, strength, and family love.</p>
        <div class="sub-heart">💐 With love from all of us 💐</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- BACKGROUND MUSIC (hidden) ----------
birthday_audio_url = "https://www.kozco.com/tech/LRMonoPhase4.wav"
audio_html = f"""
<audio id="bgMusic" autoplay loop style="display:none;">
    <source src="{birthday_audio_url}" type="audio/wav">
</audio>
<script>
    var audio = document.getElementById('bgMusic');
    audio.volume = 0.4;
    audio.play().catch(e => console.log("Autoplay prevented."));
    document.body.addEventListener('click', function() {{
        audio.play().catch(e => console.log("Still blocked."));
    }});
</script>
"""
st.markdown(audio_html, unsafe_allow_html=True)
# Optional tiny caption (can be removed if you want zero scroll)
st.caption("🎵")
