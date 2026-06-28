"""Gradio UI for the TF-IDF anime similarity recommender.
Alternative to the Streamlit app — run standalone with: python anime_gradio_ui.py
"""
import pandas as pd
import gradio as gr
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load anime dataset
try:
    anime_df = pd.read_csv("data/anime.csv", encoding="utf-8", on_bad_lines="skip")
except FileNotFoundError:
    raise FileNotFoundError(
        "anime.csv not found. Please place the full dataset at data/anime.csv.\n"
        "See data/DATA_SETUP.md for instructions."
    )

# Normalize column names (handles both 'name' and 'Name', 'genre' and 'Genres')
anime_df.columns = [c.strip() for c in anime_df.columns]
if "name" in anime_df.columns:
    anime_df.rename(columns={"name": "Name"}, inplace=True)
if "genre" in anime_df.columns:
    anime_df.rename(columns={"genre": "Genres"}, inplace=True)

anime_df = anime_df.dropna(subset=["Name"])
anime_df["Genres"] = anime_df.get("Genres", pd.Series("", index=anime_df.index)).fillna("Unknown")

# Build TF-IDF matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(anime_df["Genres"])


def recommend_anime(anime_name: str, top_n: int = 10) -> str:
    """Return top_n similar anime as formatted text."""
    name_lower = anime_name.strip().lower()
    matches = anime_df[anime_df["Name"].str.lower() == name_lower]
    if matches.empty:
        matches = anime_df[anime_df["Name"].str.lower().str.contains(name_lower, na=False)]
    if matches.empty:
        return f"No anime found matching '{anime_name}'. Try a different name."

    idx = matches.index[0]
    matched_name = anime_df.loc[idx, "Name"]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_scores[idx] = 0
    top_indices = np.argsort(sim_scores)[::-1][:top_n]

    results = [f"Top {top_n} anime similar to **{matched_name}**:\n"]
    for rank, i in enumerate(top_indices, 1):
        name = anime_df.iloc[i]["Name"]
        genres = anime_df.iloc[i]["Genres"]
        score = round(sim_scores[i], 3)
        results.append(f"{rank}. {name} | Genres: {genres} | Score: {score}")

    return "\n".join(results)


# Gradio interface
demo = gr.Interface(
    fn=recommend_anime,
    inputs=[
        gr.Textbox(label="Anime Name", placeholder="e.g. Naruto"),
        gr.Slider(minimum=5, maximum=20, value=10, step=1, label="Number of Recommendations"),
    ],
    outputs=gr.Textbox(label="Recommendations"),
    title="Anime Recommendation System (TF-IDF)",
    description="Find similar anime based on genre similarity using TF-IDF cosine similarity.",
)

if __name__ == "__main__":
    demo.launch()
