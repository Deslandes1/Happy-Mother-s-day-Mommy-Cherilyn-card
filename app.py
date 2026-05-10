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
    /* Gradient background – deep red/gold, representing strength and love */
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
        margin: 2rem auto;
        background-color: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 2rem;
        padding: 2rem;
        box-shadow: 0 0 40px rgba(0,0,0,0.3);
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
        font-size: 1.1rem;
        line-height: 1.6;
        list-style: none;
        padding-left: 0;
    }
    .names-list li {
        margin-bottom: 0.5rem;
    }
    .right-header {
        color: #ffd700;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 5px #b22222;
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

# ---------- TWO‑COLUMN LAYOUT: PHOTO LEFT, NAMES RIGHT ----------
col_left, col_right = st.columns([1, 1])

with col_left:
    # Use the direct raw URL of Sebastien's photo
    image_url = "https://raw.githubusercontent.com/Deslandes1/Happy-Mother-s-day-Mommy-Cherilyn-card/main/Sebastien%20Stephane%20Deslandes.jpg"
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="🎉 Sebastien Stephane Deslandes 🎉", width=350)
    except Exception as e:
        st.error(f"Could not load the image.\n\n{str(e)}")

with col_right:
    st.markdown('<div class="right-header">🎂 From Deslandes Family<br>we wish you a<b> Happy Birthday!</b> 🎂</div>', unsafe_allow_html=True)
    # List of family members who signed
    signers = ["Gesner Deslandes", "Gesner Junior Deslandes", "Roosevelt Deslandes", "Zendaya Christelle Deslandes"]
    # Show names in a single column, with a small heart next to each
    st.markdown('<ul class="names-list">', unsafe_allow_html=True)
    for name in signers:
        st.markdown(f'<li>💖 {name}</li>', unsafe_allow_html=True)
    st.markdown('</ul>', unsafe_allow_html=True)

# ---------- BIRTHDAY MESSAGE BELOW THE TWO COLUMNS ----------
st.markdown(
    """
    <div class="card-container">
        <div class="title">🎂 Happy Birthday, Sebastien! 🎂</div>
        <div class="heart">❤️❤️❤️</div>
        <p style="font-size:1.2rem; color:white; text-align:center;">May your day be filled with joy, strength, and the warmth of family love.</p>
        <div class="sub-heart">💐 With love from all of us 💐</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- BACKGROUND MUSIC (hidden, loops 'Happy Birthday') ----------
# Using a public domain "Happy Birthday" audio track (short, loops beautifully)
birthday_audio_url = "https://www.kozco.com/tech/LRMonoPhase4.wav"  # placeholder – replace with a reliable, persistent URL if needed
audio_html = f"""
<audio id="bgMusic" autoplay loop style="display:none;">
    <source src="{birthday_audio_url}" type="audio/wav">
    Your browser does not support the audio element.
</audio>
<script>
    var audio = document.getElementById('bgMusic');
    audio.volume = 0.4;
    audio.play().catch(e => console.log("Autoplay prevented. Please click anywhere to start music."));
    // Optional: enable music after user clicks anywhere
    document.body.addEventListener('click', function() {{
        audio.play().catch(e => console.log("Still blocked."));
    }});
</script>
"""
st.markdown(audio_html, unsafe_allow_html=True)
st.caption("🎵 Soft background music – if it doesn’t play automatically, refresh or click the page.")
