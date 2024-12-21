import streamlit as st

def main():
    st.title("Halaman Ketiga - Penjelasan tentang Collaborative Filtering")

    # Pilihan kolom
    option = st.selectbox(
        "Pilih Topik:",
        ["Apa itu Collaborative Filtering?", 
         "Cara Kerja Collaborative Filtering", 
         "Jenis-jenis Collaborative Filtering", 
         "Keuntungan dan Tantangan", 
         "Implementasi dalam Aplikasi", 
         "Contoh Penggunaan", 
         "Kesimpulan"]
    )

    # Menampilkan jawaban berdasarkan pilihan
    if option == "Apa itu Collaborative Filtering?":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            Collaborative filtering adalah teknik yang digunakan dalam sistem rekomendasi untuk memprediksi preferensi pengguna berdasarkan interaksi pengguna lain. Metode ini berfokus pada pola perilaku pengguna dan hubungan antar pengguna serta item, tanpa memerlukan informasi tambahan tentang item tersebut.
            """)

    elif option == "Cara Kerja Collaborative Filtering":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            1. **Pengumpulan Data:**
               - Data interaksi pengguna dengan item dikumpulkan, seperti rating, pembelian, atau klik. Dalam konteks aplikasi ini, data yang digunakan adalah rating yang diberikan oleh pengguna untuk berbagai tempat wisata.

            2. **Matriks Pengguna-Item:**
               - Data tersebut diorganisir dalam bentuk matriks, di mana baris mewakili pengguna dan kolom mewakili item (tempat wisata). Nilai dalam matriks adalah rating yang diberikan oleh pengguna untuk item tertentu.

            3. **Perhitungan Similarity:**
               - Menggunakan metrik seperti cosine similarity untuk menghitung kesamaan antara pengguna atau item. Dalam aplikasi ini, cosine similarity digunakan untuk menemukan pengguna yang memiliki pola rating yang mirip.

            4. **Rekomendasi:**
               - Berdasarkan kesamaan yang dihitung, sistem memberikan rekomendasi item kepada pengguna yang belum mereka interaksikan.
            """)

    elif option == "Jenis-jenis Collaborative Filtering":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            1. **User-Based Collaborative Filtering:**
               - Metode ini mencari pengguna lain yang memiliki preferensi serupa dengan pengguna yang sedang dianalisis.

            2. **Item-Based Collaborative Filtering:**
               - Metode ini berfokus pada kesamaan antar item. Rekomendasi diberikan berdasarkan item yang mirip dengan item yang telah dinilai oleh pengguna.
            """)

    elif option == "Keuntungan dan Tantangan":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            - **Keuntungan:**
              - **Tidak Memerlukan Informasi Tambahan:** Hanya bergantung pada data interaksi pengguna.
              - **Menangkap Preferensi yang Kompleks:** Dapat menangkap preferensi yang kompleks dan tidak terduga.

            - **Tantangan:**
              - **Masalah Cold Start:** Sulit memberikan rekomendasi untuk pengguna baru atau item baru.
              - **Sparsity:** Matriks pengguna-item sering kali sangat jarang, yang dapat mempengaruhi akurasi rekomendasi.
            """)

    elif option == "Implementasi dalam Aplikasi":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            Dalam aplikasi ini, collaborative filtering digunakan untuk merekomendasikan tempat wisata kepada pengguna berdasarkan rating yang diberikan oleh pengguna lain. Dengan menghitung kesamaan antara pengguna menggunakan cosine similarity, sistem dapat memberikan rekomendasi tempat wisata yang mungkin disukai oleh pengguna.
            """)

    elif option == "Contoh Penggunaan":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            - Jika pengguna A memberikan rating tinggi untuk tempat wisata X dan Y, dan pengguna B memberikan rating tinggi untuk tempat wisata Y dan Z, maka pengguna A mungkin akan direkomendasikan tempat wisata Z, karena pengguna B memiliki kesamaan dalam preferensi.
            """)

    elif option == "Kesimpulan":
        with st.expander("Lihat Penjelasan"):
            st.markdown("""
            Collaborative filtering adalah metode yang efektif untuk memberikan rekomendasi yang relevan kepada pengguna berdasarkan interaksi pengguna lain. Dengan memahami cara kerja dan penerapan metode ini, pengguna dapat lebih menghargai rekomendasi yang diberikan oleh sistem.
            """)

if __name__ == "__main__":
    main()
