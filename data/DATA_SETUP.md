# Data Setup Instructions

This repo requires **two datasets** — one per recommender engine.

---

## Tab 1 — LLM Recommender (Groq + ChromaDB)

Requires files from the `anime_recommender` repo:

| File | Source | Size | Purpose |
|---|---|---|---|
| `data/anime_with_synopsis.csv` | `anime_recommender/data/` | ~230KB | Main LLM dataset with synopsis |
| `data/anime_updated.csv` | `anime_recommender/data/` | ~234KB | Processed output of the pipeline |

### Steps:
1. Copy `anime_with_synopsis.csv` from the `anime_recommender` repo into `data/`
2. Copy `anime_updated.csv` from the `anime_recommender` repo into `data/`
3. Run the build pipeline to populate ChromaDB:
   ```bash
   python pipeline/build_pipeline.py
   ```
   This will create/populate the `chroma_db/` folder.

---

## Tab 2 — TF-IDF Cosine Similarity Recommender

Requires the full MAL anime dataset:

| File | Source | Size | Purpose |
|---|---|---|---|
| `data/anime.csv` | `Anime-Recommendation-system/anime.csv` | ~912KB | Full MAL dataset with 12,000+ anime |

### Steps:
1. Copy `anime.csv` from the `Anime-Recommendation-system` repo root into `data/`
2. The Streamlit app (Tab 2) will load it automatically.

---

## Quick Copy Commands (if you have both repos locally)

```bash
# From the combined repo root:
cp ../anime_recommender/data/anime_with_synopsis.csv data/
cp ../anime_recommender/data/anime_updated.csv data/
cp ../Anime-Recommendation-system/anime.csv data/

# Then build the vector store:
python pipeline/build_pipeline.py
```

---

## Why these files are NOT committed to git

The CSV files are large (230KB–912KB) and contain dataset content that is better
managed separately. The `.gitignore` excludes them to keep the repo lightweight.
For production deployment, use a shared volume or S3 bucket to store these files.
