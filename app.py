import streamlit as st
import pandas as pd
import numpy as np

# Tema Dashboard Modern
st.set_page_config(page_title="HTN AI Project", layout="wide")

st.title("🚀 Dashboard Analisis AI Modern")
st.write("Selamat datang di platform otomatisasi data.")

# Membuat 3 kolom metrik bergaya profesional
col1, col2, col3 = st.columns(3)
col1.metric("Proses Data", "5000+", "Aktif")
col2.metric("Kecepatan AI", "0.2ms", "-0.01ms")
col3.metric("Status Server", "Online", "Stable")

st.markdown("---")

# Grafik Interaktif
st.subheader("Visualisasi Tren Data")
data = pd.DataFrame(np.random.randn(20, 3), columns=['Analisis A', 'Analisis B', 'Analisis C'])
st.line_chart(data)

st.success("Website ini berhasil dijalankan langsung dari GitHub!")
