import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import openpyxl  # Pastikan openpyxl terinstal untuk membaca file Excel

# Load data
@st.cache
def load_data():
    try:
        df = pd.read_excel('D:\data_sciense\Data_Wisata.xlsx')  # Ganti dengan jalur file yang sesuai
        return df
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return None

# Preprocessing data
def preprocess_data(df):
    user_item_matrix = df.pivot_table(index='ID_USER', columns='TEMPAT WISATA', values='RATING').fillna(0)
    return user_item_matrix

# Calculate cosine similarity
def calculate_similarity(user_item_matrix):
    similarity_matrix = cosine_similarity(user_item_matrix)
    return similarity_matrix

# Recommend places
def recommend_places(user_id, user_item_matrix, similarity_matrix):
    user_index = user_item_matrix.index.get_loc(user_id)
    similar_users = list(enumerate(similarity_matrix[user_index]))
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:6]  # 5 pengguna teratas
    recommended_places = []

    for similar_user in similar_users:
        similar_user_index = similar_user[0]
        similar_user_ratings = user_item_matrix.iloc[similar_user_index]
        recommended_places.extend(similar_user_ratings[similar_user_ratings > 0].index.tolist())
    
    # Menghapus duplikat
    recommended_places = set(recommended_places)
    return recommended_places

# Filter places based on rating, price, and category
def filter_places_by_rating_price_and_category(df, min_rating, max_price, category):
    # Pastikan kolom HARGA memiliki tipe data numerik
    df['HARGA'] = pd.to_numeric(df['HARGA'], errors='coerce')  # Mengubah kolom HARGA menjadi numerik jika belum
    
    # Filter berdasarkan rating, harga, dan kategori
    filtered_places = df[
        (df['RATING'] >= min_rating) & 
        (df['HARGA'] <= max_price) & 
        (df['KATEGORI'] == category)
    ]
    
    # Menghapus duplikat berdasarkan TEMPAT WISATA
    filtered_places = filtered_places.drop_duplicates(subset='TEMPAT WISATA')
    
    # Mengembalikan hanya 5 tempat wisata teratas
    return filtered_places[['TEMPAT WISATA', 'KATEGORI', 'HARGA', 'RATING']].head(5)

# Get places rated by the selected user in the selected category
def get_places_rated_by_user_in_category(df, user_id, category):
    user_rated_places = df[(df['ID_USER'] == user_id) & (df['KATEGORI'] == category)]
    return user_rated_places.nlargest(5, 'RATING')

# Main function
def main():
    st.markdown('<p class="title">Sistem Rekomendasi Tempat Wisata</p>', unsafe_allow_html=True)

    # Load data
    df = load_data()
    if df is not None:
        user_item_matrix = preprocess_data(df)
        similarity_matrix = calculate_similarity(user_item_matrix)

        # Sidebar
        st.sidebar.header("Pengaturan Input")
        
        # Create a mapping of user ID to user name
        user_id_name_mapping = df[['ID_USER', 'NAMA']].drop_duplicates().set_index('ID_USER')['NAMA'].to_dict()
        selected_user_name = st.sidebar.selectbox("Pilih ID Pengguna:", list(user_id_name_mapping.keys()))
        
        # Get the corresponding user ID
        user_id = selected_user_name  # Directly use the selected user ID

        # Input category
        categories = df['KATEGORI'].unique()
        selected_category = st.sidebar.selectbox("Pilih Kategori:", categories)

        # Input manual untuk filter harga dan rating
        st.sidebar.subheader("Filter Berdasarkan Harga dan Rating")
        min_rating = st.sidebar.slider("Rating Minimum:", min_value=1, max_value=5, value=3)
        max_price = st.sidebar.number_input("Harga Maksimum:", min_value=0, step=5000, value=50000)

        # Tombol Filter
        if st.sidebar.button("Cari Wisata"):
            st.write("<p class='header'>Hasil Pencarian Berdasarkan Harga, Rating, dan Kategori</p>", unsafe_allow_html=True)
            filtered_places = filter_places_by_rating_price_and_category(df, min_rating, max_price, selected_category)
            st.dataframe(filtered_places)

            # Show the criteria used for filtering
            st.write(f"**Kriteria Pencarian:**")
            st.write(f"- Kategori: {selected_category}")
            st.write(f"- Rating Minimum: {min_rating}")
            st.write(f"- Harga Maksimum: {max_price}")

            # Show top rated places by selected category
            st.write(f"*5 Tempat Wisata Terbaik dalam Kategori '{selected_category}':*")
            top_rated_places = df[df['KATEGORI'] == selected_category].nlargest(5, 'RATING')
            st.dataframe(top_rated_places[['TEMPAT WISATA', 'KATEGORI', 'HARGA', 'RATING']])

        # Show places rated by the selected user in the selected category
        st.write(f"### Tempat Wisata yang Diberi Rating oleh {user_id_name_mapping[user_id]} dalam Kategori '{selected_category}'")
        user_rated_places_in_category = get_places_rated_by_user_in_category(df, user_id, selected_category)
        st.dataframe(user_rated_places_in_category[['TEMPAT WISATA', 'KATEGORI', 'HARGA', 'RATING']])

if __name__ == "__main__":
    main()
