#!/usr/bin/env python3
"""Generate daily inspiration quote using today's Spelling Bee answers via Kimi API."""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'answers.json')
INSPIRATION_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'inspiration.json')
KIMI_API_KEY = os.environ.get('KIMI_API_KEY', '')


def get_today_entry():
    with open(DATA_FILE) as f:
        answers = json.load(f)
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    for entry in answers:
        if entry['date'] == today:
            return entry
    # fallback to latest
    return answers[0] if answers else None


def generate_quote(entry):
    words = [w['word'] for w in entry['words']]
    pangrams = entry['pangrams']
    center = entry['centerLetter'].upper()

    prompt = (
        f"You are a creative writer. Using some of these Spelling Bee words: {', '.join(words[:15])}, "
        f"write ONE short inspiring quote (max 20 words). "
        f"Try to include the pangram word(s): {', '.join(pangrams)}. "
        f"The quote must be entirely in English — no other languages. "
        f"The quote should be uplifting, warm, and shareable. "
        f"Output ONLY the quote text, no quotation marks, no explanation."
    )

    payload = json.dumps({
        "model": "moonshot-v1-8k",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 80,
        "temperature": 0.8
    }).encode()

    req = urllib.request.Request(
        "https://api.moonshot.cn/v1/chat/completions",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {KIMI_API_KEY}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        result = json.loads(r.read())
    return result['choices'][0]['message']['content'].strip()


def main():
    if not KIMI_API_KEY:
        print("ERROR: KIMI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    entry = get_today_entry()
    if not entry:
        print("ERROR: No answer data found", file=sys.stderr)
        sys.exit(1)

    date = entry['date']
    print(f"Generating quote for {date}...")

    # Load existing inspiration data
    if os.path.exists(INSPIRATION_FILE):
        with open(INSPIRATION_FILE) as f:
            data = json.load(f)
    else:
        data = []

    # Skip if already generated today
    if any(d['date'] == date for d in data):
        print(f"{date} already has a quote, skipping")
        return

    quote = generate_quote(entry)
    print(f"Quote: {quote}")

    data.insert(0, {
        "date": date,
        "quote": quote,
        "pangrams": entry['pangrams'],
        "centerLetter": entry['centerLetter']
    })

    # Keep last 30 days
    data = data[:30]

    with open(INSPIRATION_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Saved to inspiration.json")


if __name__ == '__main__':
    main()
