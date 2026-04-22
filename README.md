# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan waktu, kondisi cuaca, dan faktor lingkungan lainnya.

## 📊 Deskripsi

Project ini bertujuan untuk mengeksplorasi data bike sharing dengan menampilkan berbagai visualisasi seperti:

* Tren penyewaan sepeda harian
* Pola penggunaan berdasarkan jam
* Pengaruh kondisi cuaca terhadap jumlah penyewaan
* Hubungan antara suhu dan aktivitas penyewaan

Dashboard ini membantu memahami perilaku pengguna serta faktor-faktor yang memengaruhi permintaan sepeda.

## ⚙️ Requirements

Pastikan sudah menginstall library berikut:

```
streamlit
pandas
plotly
```

Atau install sekaligus dengan:

```
pip install streamlit pandas plotly
```

## ▶️ Cara Menjalankan

Jalankan perintah berikut di terminal:

```
streamlit run app.py
```

## 📁 Struktur Project

```
bike-sharing-dashboard/
│
├── app.py
├── main_data.csv
├── requirements.txt
└── README.md
```

## 🚀 Fitur Utama

* KPI total penyewaan
* Visualisasi interaktif dengan Plotly
* Filter berdasarkan rentang tanggal
* Analisis berdasarkan cuaca dan waktu

## 📌 Catatan

Pastikan file `main_data.csv` berada di folder yang sama dengan `app.py`.
