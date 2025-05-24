import requests 
from bs4 import BeautifulSoup
import os
import json
import time
import random

# === CONFIG ===
START_ID = 15111
END_ID = 16110  # update this to scrape more
BATCH_SIZE = 100
DELAY_BETWEEN_BATCHES = 300  # 10 minutes
SAVE_DIR = "adaderana_articles_1000"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# === Setup ===
os.makedirs(SAVE_DIR, exist_ok=True)

def clean_text(text):
    return ' '.join(text.strip().split())

def scrape_article(article_id):
    url = f"https://sinhala.adaderana.lk/news.php?nid={article_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[{article_id}] Skipped: Request error {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    title_tag = soup.find("h1", class_="news-heading")
    date_tag = soup.find("p", class_="news-datestamp")
    content_tag = soup.find("div", class_="news-content")

    if not title_tag or not content_tag:
        print(f"[{article_id}] Skipped: Missing title or content")
        return

    title = clean_text(title_tag.get_text())
    date = clean_text(date_tag.get_text()) if date_tag else "Unknown"
    content = clean_text(content_tag.get_text())

    # Save .txt
    txt_path = os.path.join(SAVE_DIR, f"{article_id}.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"{title}\n{date}\n\n{content}")

    # Save .json
    json_path = os.path.join(SAVE_DIR, f"{article_id}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "id": article_id,
            "url": url,
            "title": title,
            "date": date,
            "content": content
        }, f, ensure_ascii=False, indent=2)

    print(f"[{article_id}] ✔️ Saved")

# === Run Scraper with batching and polite delays ===
for i, article_id in enumerate(range(START_ID, END_ID + 1), start=1):
    scrape_article(article_id)
    time.sleep(random.uniform(2, 4))  # polite delay between articles

    # Pause after each batch
    if i % BATCH_SIZE == 0 and article_id != END_ID:
        print(f"\n🕒 Batch complete. Waiting {DELAY_BETWEEN_BATCHES // 60} minutes before next batch...\n")
        time.sleep(DELAY_BETWEEN_BATCHES)
