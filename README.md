# IMDB Suggestion

A small NLP project that recommends movies based on plot similarity. The repository includes a dataset scraped from IMDb as well as scripts for generating recommendations.

## Features
- Scrape plot summaries from IMDb with `web_scraping.py` (requires internet access).
- Clean text by removing punctuation and stop words via NLTK.
- Compute TF‑IDF vectors for each movie summary.
- Recommend similar titles using cosine similarity.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. **Update the dataset** (optional):
   ```bash
   python web_scraping.py
   ```
   This creates `data.csv` with plots from the IMDb Top 250 list. The project already includes a dataset so this step can be skipped when offline.

2. **Find similar movies**:
   ```bash
   python main_proj.py
   ```
   Provide a short plot description when prompted and the script will print a list of movies with the highest similarity scores.

## Dataset
`data.csv` ships with roughly 250 cleaned movie summaries so the recommendation script can run without performing web scraping.

## Project status
This code was originally created for a university course and is provided as‑is. Feel free to adapt it for your own experiments.
