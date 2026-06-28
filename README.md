# 🎌 Anime Recommender — Combined

A unified Anime Recommendation System combining two approaches in one Streamlit app:

| Tab | Engine | Source Repo |
|-----|--------|-------------|
| 🤖 AI Recommender | Groq LLM + ChromaDB + LangChain RAG | `anime_recommender` |
| 📊 Similarity Search | TF-IDF + Cosine Similarity | `Anime-Recommendation-system` |

## 🚀 Setup

### 1. Clone & install
```bash
git clone https://github.com/Shrikant-Bawankule/anime-recommender-combined.git
cd anime-recommender-combined
pip install -r requirements.txt
```

### 2. Add your API key
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 3. Add anime.csv to data/
- Download `anime.csv` from [Kaggle MyAnimeList dataset](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)
- Place it at `data/anime.csv`

### 4. Build ChromaDB vector store (for Tab 1 only)
```bash
python pipeline/build_pipeline.py
```

### 5. Run the app
```bash
streamlit run app/app.py
```

## 📁 Project Structure
```
anime-recommender-combined/
├── app/
│   └── app.py              # Main Streamlit app (2 tabs)
├── pipeline/
│   ├── pipeline.py         # LLM pipeline class
│   └── build_pipeline.py   # Build ChromaDB vector store
├── src/
│   ├── data_loader.py      # CSV loader + preprocessing
│   ├── vector_store.py     # ChromaDB builder & loader
│   ├── recommender.py      # LangChain RAG chain
│   └── prompt_template.py  # Groq prompt
├── config/
│   └── config.py           # API key + model config
├── utils/
│   ├── logger.py
│   └── custom_exception.py
├── data/                   # Place anime.csv here
├── chroma_db/              # Auto-generated after build
├── .env.example
├── requirements.txt
└── setup.py
```
