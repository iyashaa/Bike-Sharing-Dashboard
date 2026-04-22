import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
from babel.numbers import format_currency

# Helper function untuk menyiapkan data trend
def create_monthly_orders_df(df):
    monthly_orders_df = df.groupby(by="month_year").agg({
        "total_orders": "sum",
        "revenue": "sum"
    }).reset_index()
    return monthly_orders_df

# Helper function untuk kategori produk
def create_category_performance_df(df):
    category_performance_df = df.groupby(by="product_category_name_english").agg({
        "total_orders": "sum",
        "revenue": "sum"
    }).sort_values(by="total_orders", ascending=False).reset_index()
    return category_performance_df

# Load cleaned data
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "main_data.csv")

main_df = pd.read_csv(file_path)

# Pastikan kolom waktu dalam format datetime
main_df["month_year"] = pd.to_datetime(main_df["month_year"]).dt.date
main_df.sort_values(by="month_year", inplace=True)

# Filter Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Rentang waktu
    min_date = main_df["month_year"].min()
    max_date = main_df["month_year"].max()
    
    date_range = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        st.warning("Silakan pilih rentang tanggal dengan lengkap.")
        st.stop()

    if start_date > end_date:
        st.error("Rentang tanggal tidak valid!")
        st.stop()


# Filter data berdasarkan pilihan sidebar
filtered_df = main_df[(main_df["month_year"] >= start_date) & 
                       (main_df["month_year"] <= end_date)]

# Menyiapkan data untuk visualisasi
monthly_orders_df = create_monthly_orders_df(filtered_df)
category_df = create_category_performance_df(filtered_df)

# Header Dashboard
st.header('E-Commerce Public Dashboard :sparkles:')

# Section 1: Metrics
st.subheader('Daily Orders')
col1, col2 = st.columns(2)

with col1:
    total_orders = monthly_orders_df.total_orders.sum()
    st.metric("Total Orders", value=total_orders)

with col2:
    total_revenue = format_currency(monthly_orders_df.revenue.sum(), "BRL", locale='pt_BR') 
    st.metric("Total Revenue", value=total_revenue)

# Section 2: Trend Penjualan
st.subheader("Busiest Month for Orders")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_orders_df["month_year"],
    monthly_orders_df["total_orders"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Section 3: Performa Kategori Produk
st.subheader("Best & Worst Performing Product Category")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Best Performing
sns.barplot(x="total_orders", y="product_category_name_english", data=category_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

# Worst Performing
sns.barplot(x="total_orders", y="product_category_name_english", data=category_df.sort_values(by="total_orders", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

# Footer Identitas
st.caption('Copyright (C) Ghiyyas Abiyasha Winardi (50423537 - 3IA20) 2026')