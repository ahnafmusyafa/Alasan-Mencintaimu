import streamlit as st
import random

data_cinta = [
    {"alasan": "Karena berdua bersamamu mengajarkanku apa artinya kenyamanan, kesempurnaan, cintaaa.", "lagu": "kesempurnaancinta.mp3"},
    {"alasan": "Karena kamulah satu-satunya yang mengerti aku.", "lagu": "satusatunya.mp3"},
    {"alasan": "Karena duniaku menjadi semakin terang benderang.", "lagu": "jikabersamamu.mp3"},
    {"alasan": "karena to die by your side is such a heavenly way to die", "lagu": "thesmiths.mp3"},
    {"alasan": "Karena kau begitu sempurna, dimataku kau begitu indah.", "lagu": "sempurna.mp3"}
]

st.set_page_config(page_title="Untuk Nana", page_icon="💖")

st.title("💖 This is For You Nana 💖")
st.write("Hai sayang...")
st.write("Setiap kali kamu tekan tombol di bawah, aku akan kasih satu alasan kenapa aku sayang kamu...")
st.divider()

if 'data_tersisa' not in st.session_state:
    st.session_state.data_tersisa = data_cinta.copy()
    random.shuffle(st.session_state.data_tersisa)

if st.button("Tekan untuk alasan berikutnya ❤️"):
    if st.session_state.data_tersisa:
        paket = st.session_state.data_tersisa.pop()
        
        st.subheader("✨ Aku sayang kamu...")
        st.write(f"...{paket['alasan']}")
        
        nama_file_lagu = paket['lagu']
        try:
            with open(nama_file_lagu, 'rb') as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.caption("Psst... tekan tombol ▶️ di atas untuk mendengarkan lagunya 😉")
        except FileNotFoundError:
            st.error(f"Error: File lagu '{nama_file_lagu}' tidak ditemukan. Pastikan sudah diunggah dengan benar ke GitHub.")
        # --------------------------------

    else:
        st.success("Alasanku sudah habis untuk sekarang, tapi cintaku tidak akan pernah. ❤️")
        st.balloons()
