import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- POSTER FUNCTION ----------------
def fetch_poster(movie_title):
    api_key = "7632fb89"   # OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    data = requests.get(url).json()

    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Poster"

# ---------------- RECOMMENDER ----------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))

    return names, posters

# ---------------- STREAMLIT UI ----------------
st.set_page_config(layout="wide")
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
