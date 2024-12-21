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
    user_item_matrix = df.pivot_table(index='ID_USER', columns='ID_TEMPAT', values='RATING').fillna(0)
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
    
    return set(recommended_places)  # Mengembalikan tempat yang unik

# Get top rated places by category
def get_top_rated_places_by_category(df, category, top_n=5):
    filtered_df = df[df['KATEGORI'] == category]
    top_rated_places = filtered_df.nlargest(top_n, 'RATING')
    return top_rated_places

# Get places rated by user in a specific category
def get_places_rated_by_user_in_category(df, user_id, category):
    user_rated_places = df[(df['ID_USER'] == user_id) & (df['KATEGORI'] == category)]
    return user_rated_places.nlargest(5, 'RATING')

# Main function
def main():
    st.title("Sistem Rekomendasi Tempat Wisata")
    
    # Load data
    df = load_data()
    if df is not None:
        user_item_matrix = preprocess_data(df)
        similarity_matrix = calculate_similarity(user_item_matrix)

        # Create a mapping of user ID to user name
        user_id_name_mapping = df[['ID_USER', 'NAMA']].drop_duplicates().set_index('ID_USER')['NAMA'].to_dict()

        # Input user ID
        selected_user_name = st.selectbox("Pilih Nama Pengguna:", list(user_id_name_mapping.values()))
        
        # Get the corresponding user ID
        user_id = [key for key, value in user_id_name_mapping.items() if value == selected_user_name][0]

        # Input category
        categories = df['KATEGORI'].unique()
        selected_category = st.selectbox("Pilih Kategori:", categories)

        if st.button("Dapatkan Rekomendasi"):
            recommendations = recommend_places(user_id, user_item_matrix, similarity_matrix)
            st.write("Rekomendasi Tempat Wisata untuk Anda:")
            
            # Show top rated places by selected category
            st.write(f"5 Tempat Wisata Terbaik dalam Kategori '{selected_category}':")
            top_rated_places = get_top_rated_places_by_category(df, selected_category)
            st.dataframe(top_rated_places[['TEMPAT WISATA', 'KATEGORI', 'HARGA', 'RATING']])

            # Show places rated by the selected user in the selected category
            st.write(f"Tempat Wisata dengan Rating Tertinggi oleh Rekomendasi User dalam Kategori '{selected_category}':")
            user_rated_places_in_category = get_places_rated_by_user_in_category(df, user_id, selected_category)
            st.dataframe(user_rated_places_in_category[['TEMPAT WISATA', 'KATEGORI', 'HARGA', 'RATING']])

if __name__ == "__main__":
    main()
