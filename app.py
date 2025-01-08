import streamlit as st
from time import sleep
from models.model import predict  # Mengimpor fungsi predict dari model.py di folder models

# Pengaturan halaman
st.set_page_config(
    page_title="Hoax Classification",
    layout="centered",
    page_icon=":red_car:"
)

st.title("Hoax Classification")
st.write("Aplikasi ini membantu mengklasifikasikan apakah suatu teks mengandung hoax atau tidak.")

# Input teks dari pengguna
input_text = st.text_area("Masukkan teks untuk klasifikasi:", height=100)

if st.button("Klasifikasikan"):
    if input_text:
        # Menampilkan progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        status_text.text("Sedang memproses...")

        for percent in range(101):
            sleep(0.03)
            progress_bar.progress(percent)

        status_text.text("Proses selesai!")

        # Memanggil fungsi predict dari models/model.py
        try:
            result = predict(input_text)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
            result = None

        # Menampilkan hasil klasifikasi
        if result:
            st.subheader("Hasil Klasifikasi:")
            if result == "Hoax":
                st.markdown(
                    f"""
                    <div style="color: white; background-color: red; font-size: 20px; border-radius: 12px; padding: 10px; text-align: center; width: fit-content;">
                        <b>{result}</b>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="color: white; background-color: green; font-size: 20px; border-radius: 12px; padding: 10px; text-align: center; width: fit-content;">
                        <b>{result}</b>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        else:
            st.error("Tidak dapat mengklasifikasikan teks. Periksa input Anda.")

        sleep(1)
        progress_bar.empty()
        status_text.empty()
    else:
        st.error("Harap masukkan teks sebelum melakukan klasifikasi.")

st.caption("--------")
st.caption(
    "Disclaimer: Jangan percaya prediksi ini 100%. Selalu coba mencari informasi lebih lanjut untuk memastikan kebenaran."
)