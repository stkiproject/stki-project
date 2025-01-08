# Hoax Classification

Project klasifikasi berita hoax bahasa Indonesia menggunakan machine learning. Terdapat antarmuka pengguna untuk memasukkan teks narasi dan mendapatkan prediksi apakah narasi tersebut hoax atau tidak.

## Project Structure

```
hoax-classification
├── app.py                       # File utama aplikasi Streamlit
├── models
│   ├── classification.ipynb     # Notebook untuk eksplorasi dan pelatihan model
│   ├── data_preprocessed.csv    # Dataset yang sudah dipreproses
│   ├── model.py                 # Implementasi model klasifikasi
│   ├── multinomial_nb_model.pkl # Model yang sudah dilatih
│   └── tfidf_vectorizer.pkl     # Vectorizer yang sudah dilatih
├── data
│   ├── Data_latih.csv           # Dataset training
│   ├── Data_uji.csv             # Dataset testing
│   └── README.md                # Dokumentasi dataset
├── requirements.txt             # Dependency Python untuk proyek
└── README.md                    # Dokumentasi proyek
```

## Cara Install

1. Clone repository

2. Install package yang dibutuhkan:
   ```sh
   pip install -r requirements.txt
   ```

## Penggunaan

Untuk menjalankan aplikasi Streamlit, jalankan perintah berikut:

```sh
streamlit run app.py
```

Buka browser dan masukkan URL `http://localhost:8501` untuk mengakses aplikasi.

## Penjelasan Proses Machine Learning
