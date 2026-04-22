import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set konfigurasi halaman Streamlit
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")

# Fungsi untuk memuat data (menggunakan cache agar lebih cepat)
@st.cache_data
def load_data():

    base_dir = os.path.dirname(__file__)

    file_path = os.path.join(base_dir, "main_data.csv")
    df = pd.read_csv(file_path)
    # Konversi kolom dteday menjadi tipe datetime
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# --- SIDEBAR ---
st.sidebar.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=500)
st.sidebar.title("Filter Berdasarkan Rentang Waktu")

# Filter Rentang Tanggal
min_date = df['dteday'].min()
max_date = df['dteday'].max()

try:
    start_date, end_date = st.sidebar.date_input(
        label="Pilih Rentang Waktu",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
except ValueError:
    st.error("Silakan pilih rentang tanggal yang valid!")
    st.stop()

# Terapkan filter ke dataframe utama
main_df = df[(df['dteday'] >= pd.to_datetime(start_date)) & 
             (df['dteday'] <= pd.to_datetime(end_date))]

# --- HEADER & KPI ---
st.title("🚲 Dashboard Analisis Bike Sharing")
st.markdown("Visualisasi interaktif untuk menganalisis pola penyewaan sepeda berdasarkan waktu dan kondisi lingkungan.")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    total_rentals = main_df['cnt'].sum()
    st.metric("Total Peminjaman", value=f"{total_rentals:,}")

with col2:
    total_registered = main_df['registered'].sum()
    st.metric("Pengguna Terdaftar (Registered)", value=f"{total_registered:,}")

with col3:
    total_casual = main_df['casual'].sum()
    st.metric("Pengguna Kasual (Casual)", value=f"{total_casual:,}")

st.markdown("---")

# --- VISUALISASI UTAMA ---

# 1. Tren Peminjaman Harian (Line Chart)
st.subheader("📈 Tren Peminjaman Sepeda Harian")
daily_rent_df = main_df.groupby('dteday').agg({'cnt': 'sum', 'casual': 'sum', 'registered': 'sum'}).reset_index()

fig_daily = go.Figure()
fig_daily.add_trace(go.Scatter(x=daily_rent_df['dteday'], y=daily_rent_df['cnt'], mode='lines', name='Total', line=dict(color='blue', width=2)))
fig_daily.add_trace(go.Scatter(x=daily_rent_df['dteday'], y=daily_rent_df['registered'], mode='lines', name='Registered', line=dict(color='green', width=1, dash='dot')))
fig_daily.add_trace(go.Scatter(x=daily_rent_df['dteday'], y=daily_rent_df['casual'], mode='lines', name='Casual', line=dict(color='orange', width=1, dash='dot')))

fig_daily.update_layout(xaxis_title="Tanggal", yaxis_title="Jumlah Peminjaman", hovermode="x unified")
st.plotly_chart(fig_daily, use_container_width=True)

# Membagi layar menjadi 2 kolom untuk visualisasi berikutnya
col_viz1, col_viz2 = st.columns(2)

# 2. Pola Peminjaman Berdasarkan Jam (Line Chart)
with col_viz1:
    st.subheader("⏰ Pola Peminjaman per Jam")
    hourly_rent_df = main_df.groupby('hr')['cnt'].mean().reset_index()
    
    fig_hourly = px.line(hourly_rent_df, x='hr', y='cnt', markers=True, 
                         labels={'hr': 'Jam (0-23)', 'cnt': 'Rata-rata Peminjaman'},
                         color_discrete_sequence=["#FF4B4B"])
    fig_hourly.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=1))
    st.plotly_chart(fig_hourly, use_container_width=True)

# 3. Peminjaman Berdasarkan Cuaca (Bar Chart)
with col_viz2:
    st.subheader("☁️ Rata-rata Peminjaman by Cuaca")
    weather_rent_df = main_df.groupby('weathersit')['cnt'].mean().reset_index()
    weather_rent_df = weather_rent_df.sort_values(by='cnt', ascending=False)
    
    fig_weather = px.bar(weather_rent_df, x='weathersit', y='cnt', 
                         color='weathersit',
                         labels={'weathersit': 'Kondisi Cuaca', 'cnt': 'Rata-rata Peminjaman'})
    st.plotly_chart(fig_weather, use_container_width=True)

# 4. Pengaruh Suhu terhadap Peminjaman (Scatter Plot)
st.subheader("🌡️ Pengaruh Suhu Terhadap Jumlah Peminjaman")
fig_temp = px.scatter(main_df, x='temp', y='cnt', color='season', hover_data=['dteday', 'hr'],
                      labels={'temp': 'Suhu (Normalisasi)', 'cnt': 'Jumlah Peminjaman', 'season': 'Musim'},
                      opacity=0.6)
st.plotly_chart(fig_temp, use_container_width=True)

# Footer
st.caption("Copyright (C) Ghiyyas Abiyasha Winardi")