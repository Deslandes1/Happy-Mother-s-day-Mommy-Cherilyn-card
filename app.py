import streamlit as st
import base64
from datetime import datetime
import os

st.set_page_config(
    page_title="Happy Birthday, Mommy Cherilyn!",
    page_icon="🎂",
    layout="wide"
)

# ========== CUSTOM CSS: BLUE SHINING BACKGROUND WITH STARS ==========
st.markdown(
    """
    <style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(135deg, #0b3d91, #1e90ff, #87cefa, #0b3d91);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
        position: relative;
        overflow: hidden;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Twinkling stars */
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }
    .star {
        position: absolute;
        background-color: white;
        border-radius: 50%;
        opacity: 0;
        animation: twinkle 3s infinite;
    }
    @keyframes twinkle {
        0% { opacity: 0; transform: scale(0.5); }
        50% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(0.5); }
    }
    /* Content container */
    .main-content {
        position: relative;
        z-index: 2;
        text-align: center;
        padding: 2rem;
    }
    .title {
        font-size: 4rem;
        font-weight: bold;
        color: #fff9c4;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffaa00;
        margin-bottom: 1rem;
    }
    .names-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
    }
    .name-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
        border-radius: 50px;
        padding: 0.8rem 1.5rem;
        font-size: 1.3rem;
        font-weight: bold;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 0 15px rgba(255, 255, 200, 0.5);
        transition: transform 0.2s;
    }
    .name-card:hover {
        transform: scale(1.05);
        background: rgba(255, 215, 0, 0.5);
    }
    .heart {
        font-size: 3rem;
        animation: heartbeat 1s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .photo-caption {
        font-size: 1.2rem;
        font-weight: bold;
        color: #fff9c4;
        margin-top: -0.5rem;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 5px #ffaa00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generate random stars
star_js = """
<script>
(function() {
    const starContainer = document.createElement('div');
    starContainer.className = 'stars';
    document.body.appendChild(starContainer);
    
    for (let i = 0; i < 200; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        const size = Math.random() * 4 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 5 + 's';
        star.style.animationDuration = Math.random() * 3 + 2 + 's';
        starContainer.appendChild(star);
    }
})();
</script>
"""
st.markdown(star_js, unsafe_allow_html=True)

# ---------- MAIN CONTENT ----------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎂 Happy Birthday, Mommy Cherilyn! 🎂</div>', unsafe_allow_html=True)

# --- LOCAL IMAGE FILE (supports multiple possible names) ---
possible_filenames = ["cherylenn", "cherylenn.jpeg", "cherylenn.jpg", "cherylenn.png"]

image_file = None
for fname in possible_filenames:
    if os.path.exists(fname):
        image_file = fname
        break

if image_file:
    st.image(image_file, caption="💖 Mommy Cherilyn – Our Beautiful Queen 💖", width='stretch')
else:
    st.error("❌ Could not find the image file. Please upload a photo named 'cherylenn' (with or without extension like .jpeg, .jpg, .png) to the same folder as app.py.")
    st.info("Make sure the file name is exactly as you typed: 'cherylenn' (case‑sensitive).")

# ---------- LIST OF LOVING NAMES ----------
names = [
    "Sandiana Septembre", "Daffecat Michel", "Sophonia Darius", "Marie Prisca Rodney",
    "Volmar Lovena", "Daya Joachim", "Horlinne François", "Shelove Polisca",
    "Isselande Miselin", "Nashca Pierre", "Pierre Louis Guerlanda", "Djoudemie Jean Baptiste",
    "Isemylove Galioth", "Christie Paul", "Valentina Etienne", "Dapheka Jeanlubin",
    "Daphené Jeanlubin", "Soriya Mérisme", "Rose Mania François", "Anie François",
    "Dieuna Robert", "Woodshaina Bolivar", "Bedsaida Louis", "Solaika", "Djemaya"
]

st.markdown('<div class="names-container">', unsafe_allow_html=True)
for name in names:
    st.markdown(f'<div class="name-card">💖 {name} 💖</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Heart animation
st.markdown('<div class="heart">❤️❤️❤️</div>', unsafe_allow_html=True)
st.markdown("<h2 style='color:white;'>We love you and celebrate you today!</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color:white; font-size:1.2rem;'>📅 {datetime.now().strftime('%B %d, %Y')}</p>", unsafe_allow_html=True)

# ---------- BACKGROUND MUSIC (optional) ----------
st.markdown("---")
st.markdown("<h3 style='color:white;'>🎵 Listen to a classic Happy Birthday song 🎵</h3>", unsafe_allow_html=True)

audio_file = "happy_birthday_song.mp3"
try:
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio id="bgMusic" controls autoplay loop style="width:100%; max-width:400px; margin:0 auto; display:block;">
        <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    <script>
        var audio = document.getElementById('bgMusic');
        audio.play().catch(e => console.log("Autoplay prevented."));
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
    st.caption("🎶 If the music doesn’t play automatically, click the ▶️ button above. 🎶")
except Exception:
    st.warning("🎧 Optional: Add a Happy Birthday song file named 'happy_birthday_song.mp3' to this folder.")

# Extra love note
st.markdown(
    """
    <div style="background: rgba(0,0,0,0.4); border-radius: 20px; padding: 1rem; margin-top: 2rem;">
        <p style="color:#fff9c4; font-size:1.2rem;">✨ Happy Birthday, Mommy Cherilyn! ✨</p>
        <p style="color:white;">💐 You are loved by all these names and more. Have a blessed day! 💐</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
