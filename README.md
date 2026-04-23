# Bike Sharing Dashboard

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan waktu, cuaca, dan faktor lingkungan lainnya.

---
# Deskripsi

Project ini bertujuan untuk mengeksplorasi data bike sharing dengan menampilkan berbagai visualisasi seperti:

* Tren penyewaan sepeda harian
* Pola penggunaan berdasarkan jam
* Pengaruh kondisi cuaca terhadap jumlah penyewaan
* Hubungan antara suhu dan aktivitas penyewaan

Dashboard ini membantu memahami perilaku pengguna serta faktor-faktor yang memengaruhi permintaan sepeda.
---
## Setup Environment - Anaconda

```bash
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt
```

---

## Setup Environment - Shell/Terminal

```bash
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶Menjalankan Aplikasi Streamlit

```bash
streamlit run dashboard.py
```

---

## Requirements

Library yang digunakan dalam project ini:

```txt
streamlit
pandas
plotly
numpy
matplotlib
seaborn
```

---

## Struktur Project

```
bike-sharing-dashboard
│
|──── dashboard
|    ├── dashboard.py
|    └── main_data.csv
|──── data
|    ├── day.csv
|    └── hour.csv
├── requirements.txt
|── url.txt
|── notebook.ipynb
└── README.md
```

---

## Fitur Dashboard

* Visualisasi tren penyewaan sepeda harian
* Analisis pola penyewaan berdasarkan jam
* Perbandingan penyewaan berdasarkan kondisi cuaca
* Analisis pengaruh suhu terhadap jumlah penyewaan
* KPI total pengguna (casual & registered)

---

## Catatan

Pastikan file `main_data.csv` berada dalam direktori yang sama dengan `dashboard.py` agar aplikasi dapat berjalan dengan baik.
