# Prompt Generator

A minimal web interface that lets a user type a prompt and optionally upload an image. Each entry is stored in a tiny SQLite database.

## How to run
1. Make sure you have Python 3.9+ installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the app:
   ```
   python app.py
   ```
4. Open a browser at `http://127.0.0.1:5000/`.

## Project structure
```
prompt_ai/
│   app.py               # Flask server, DB handling
│   requirements.txt      # Python packages
│   README.md             # This file
│
├───templates
│       index.html       # Simple UI
│
└───static
    └───uploads          # Uploaded images (created at runtime)
```

## Presentation guide
- **Goal** – Show how the IA can generate a prompt based on user‑provided text and an optional image.
- **Demo steps**
  1. Open the web page.
  2. Fill the *Prompt text* field.
  3. (Optional) attach an image.
  4. Click **Save** – the page refreshes and the new entry appears below.
- **Talking points**
  - Simple Flask + SQLite keeps the implementation lightweight.
  - The UI is pure HTML/CSS – no JavaScript frameworks needed.
  - All data is stored locally; no external services are required.
- **What to emphasise**
  - Clean separation: UI (templates) vs. data layer (SQLite).
  - Extensibility – the DB can be expanded with more columns (e.g., generation parameters) without changing the core logic.

Feel free to adapt the wording for your presentation slide deck.
