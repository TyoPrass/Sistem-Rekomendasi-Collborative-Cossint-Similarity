import streamlit as st

st.set_page_config(page_title="Sistem Rekomendasi Tempat Wisata", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ("Rekomendasi Tempat Wisata", "Input Rating dan Filter", "Penjelasan Terkait Metode"))

if page == "Rekomendasi Tempat Wisata":
    import page1  # Halaman pertama
    page1.main()
elif page == "Input Rating dan Filter":
    import page2  # Halaman kedua
    page2.main()
else:
    import page3  # Halaman ketiga
    page3.main()
