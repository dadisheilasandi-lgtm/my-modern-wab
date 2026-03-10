import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="HTN Data Processor", layout="wide")

st.title("🚀 HTN AI: Smart Data Processor")
st.markdown("Unggah file Excel atau CSV Anda untuk dianalisis secara instan.")

# Fitur Upload File
uploaded_file = st.file_uploader("Pilih file (CSV atau Excel)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Membaca data berdasarkan formatnya
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Menampilkan Metrik Otomatis
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Baris Data", len(df))
        col2.metric("Total Kolom", len(df.columns))
        col3.metric("Status", "Siap Diproses")

        st.markdown("---")

        # Menampilkan Preview Data
        st.subheader("Preview Data Anda:")
        st.dataframe(df.head(10)) # Menampilkan 10 baris pertama

        # Grafik Sederhana (Jika ada data numerik)
        st.subheader("Visualisasi Cepat")
        st.area_chart(df.select_dtypes(include=['number']))

    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")

else:
    st.info("Menunggu file diunggah... Silakan pilih file Excel/CSV dari laptop Anda.")
