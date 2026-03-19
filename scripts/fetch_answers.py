#!/usr/bin/env python3
"""
Fetch today's NYT Spelling Bee answers from NYT page (window.gameData)
and update data/answers.json
"""
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone

def fetch_game_data():
    url = "https://www.nytimes.com/puzzles/spelling-bee"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode("utf-8")

    m = re.search(r'window\.gameData\s*=\s*(\{.*?\})\s*</script>', html, re.DOTALL)
    if not m:
        raise ValueError("gameData not found in page")

    return json.loads(m.group(1))

def main():
    print("Fetching from NYT...")
    game_data = fetch_game_data()
    today = game_data.get("today", {})

    date_iso = today.get("printDate")
    center = today.get("centerLetter", "").upper()
    outer = [l.upper() for l in today.get("outerLetters", [])]
    pangrams = [w.upper() for w in today.get("pangrams", [])]
    answers = [w.upper() for w in today.get("answers", [])]

    print(f"Date: {date_iso}, Center: {center}, Words: {len(answers)}, Pangrams: {pangrams}")

    if not answers:
        print("ERROR: No answers found")
        sys.exit(1)

    word_entries = [
        {
            "word": w,
            "isPangram": w in pangrams,
            "definition": "",
            "partOfSpeech": ""
        }
        for w in answers
    ]

    new_entry = {
        "date": date_iso,
        "centerLetter": center,
        "outerLetters": outer,
        "pangrams": pangrams,
        "words": word_entries,
    }

    data_path = "data/answers.json"
    with open(data_path, "r") as f:
        existing = json.load(f)

    if any(a["date"] == date_iso for a in existing):
        print(f"{date_iso} already exists, skipping")
        return

    existing.insert(0, new_entry)
    existing = existing[:365]

    with open(data_path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"✓ Updated {data_path} with {date_iso} ({len(answers)} words)")

if __name__ == "__main__":
    main()
