# 🎬 Movie Recommender System

A **content-based movie recommender system** built using **Python and Streamlit**.  
The application recommends movies similar to a selected movie and displays their posters in an interactive web interface.

🔗 **Live Demo:** https://priyrajsinh-final-movie-rec.hf.space

---

## 📌 Project Overview

This project demonstrates an end-to-end implementation of a movie recommendation system:
- Data preprocessing and feature engineering
- Similarity-based recommendation logic
- Interactive web application using Streamlit
- Public deployment with a shareable URL

The goal of this project is to understand **recommendation systems** and build a **complete ML-based application**.

---

## 🚀 Features

- Select a movie from a dropdown list
- Get top 5 similar movie recommendations
- Dynamically fetch and display movie posters
- Simple and interactive Streamlit UI
- Publicly deployed live demo

---

## 🛠 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Streamlit**
- **Pickle**
- **OMDb API** (for movie posters)

---

## 🧠 How the Recommendation Works

1. Movie metadata is processed and vectorized.
2. A **similarity matrix** is computed using cosine similarity.
3. When a movie is selected:
   - The system finds the most similar movies.
   - Corresponding movie posters are fetched via the OMDb API.
4. Results are displayed in the Streamlit application.

---
final_movie_rec/
│
├── app.py # Streamlit application
├── movie_dict.pkl # Processed movie metadata
├── similarity.pkl # Precomputed similarity matrix
├── movie_recommender_model.ipynb # Notebook used to build the model (optional)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📦 About the `.pkl` Files

This project uses **pickle (`.pkl`) files** to store preprocessed data and model outputs.

### `movie_dict.pkl`
- Contains processed movie metadata (titles, IDs, features, etc.)
- Created after cleaning and preparing the movie dataset
- Loaded directly by the Streamlit app

### `similarity.pkl`
- Contains a precomputed similarity matrix
- Generated using cosine similarity on movie feature vectors
- Allows fast recommendation without recomputing similarities

These files are generated **once** and reused by the application for efficiency.

---

## 🧪 How the `.pkl` Files Were Created

The `.pkl` files were generated using the Jupyter notebook:

movie_recommender_model.ipynb


This notebook includes:
- Data loading and preprocessing
- Feature extraction
- Similarity computation
- Saving processed outputs using `pickle`

Example snippet used in the notebook:

```python
import pickle

pickle.dump(movie_dict, open("movie_dict.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

▶️ Run the Project Locally
1️⃣ Clone the repository

pip install -r requirements.txt

streamlit run app.py

The app will open automatically in your browser.

🌐 Deployment

The application is deployed on Hugging Face Spaces, which provides a free and public hosting platform for Streamlit apps.

🔗 Live Demo:

📚 Learning Outcomes

Built a content-based recommendation system

Understood similarity metrics and feature engineering

Developed a Streamlit-based ML web app

Learned how to deploy ML applications publicly

Improved end-to-end ML project understanding

📈 Future Improvements

Add collaborative filtering

Improve recommendation accuracy

Enhance UI/UX

Add user ratings and feedback

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements

Streamlit for the UI framework

OMDb API for movie poster data

Open-source movie datasets
## 📂 Project Structure

