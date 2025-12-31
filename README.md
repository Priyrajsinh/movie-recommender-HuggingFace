# 🎬 Movie Recommender System

A content-based movie recommender system built using Python and Streamlit.
The application recommends movies similar to a selected movie and displays their posters in an interactive web interface.

Live Demo: https://priyrajsinh-final-movie-rec.hf.space

---

## Project Overview

This project demonstrates an end-to-end implementation of a movie recommendation system, from data preprocessing to deployment.
It focuses on similarity-based recommendations and building an interactive ML-powered web application.

---

## Features

- Select a movie from a dropdown list
- Get top 5 similar movie recommendations
- Dynamically fetch and display movie posters
- Clean and interactive Streamlit interface
- Publicly deployed live demo

---

## Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Pickle
- OMDb API (for movie posters)

---

## How the Recommendation Works

1. Movie metadata is processed and vectorized.
2. A similarity matrix is computed using cosine similarity.
3. When a user selects a movie:
   - The system finds the most similar movies.
   - Movie posters are fetched using the OMDb API.
4. Results are displayed in the Streamlit application.

---

## Project Structure

final_movie_rec/
│
├── app.py                         # Streamlit application
├── movie_dict.pkl                 # Processed movie metadata
├── similarity.pkl                 # Precomputed similarity matrix
├── movie_recommender_model.ipynb  # Notebook used to build the model (optional)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

---

## About the .pkl Files

This project uses precomputed .pkl files to improve performance and avoid recomputing data at runtime.

movie_dict.pkl:
- Stores processed movie metadata
- Created after data cleaning and preprocessing
- Used by the Streamlit app to populate movie selections

similarity.pkl:
- Stores the cosine similarity matrix
- Used to find similar movies efficiently
- Loaded directly by the application

---

## How the .pkl Files Were Created

The .pkl files were created using a Jupyter Notebook:

movie_recommender_model.ipynb

Example code used:

import pickle
pickle.dump(movie_dict, open("movie_dict.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

---

## Run the Project Locally

pip install -r requirements.txt
streamlit run app.py

---

## Deployment

The application is deployed on Hugging Face Spaces.

Live Demo: https://priyrajsinh-final-movie-rec.hf.space

---

## License

MIT License
