# Advanced DuckDuckGo Dorker GUI (KAVASRI)

**Short summary**  
Advanced DuckDuckGo Dorker is a lightweight cross‑platform GUI tool built with Python/Tkinter to compose and launch complex DuckDuckGo search queries (dorks) quickly. Ideal for research, open‑source intelligence (OSINT) learning, advanced search workflows, and productivity.

---

## Key features
- GUI form to build DuckDuckGo queries with common dork operators:
  - `intitle:`, `inurl:`, `filetype:`, `site:`, `-site:`, exact phrase, and exclude terms.
- Live generated query preview (copy to clipboard).
- One‑click open in default browser (DuckDuckGo).
- Simple, dependency‑light, designed for clarity & education.

---

## Why this repo
This app helps researchers, pentesters (ethical), and curious makers quickly build precise search strings without memorizing operator syntax. It’s minimal, portable, and great for demos or learning OSINT responsibly.

---

## Quick demo
1. Enter main search term(s).
2. Optionally fill `intitle`, `inurl`, `filetype`, etc.
3. Click **Generate & Search** — your query opens in DuckDuckGo.
4. Use **Copy Query** to paste into other tools or notes.

---

## Installation

**Prerequisites**
- Python 3.8+ (recommended 3.10+)
- `tkinter` (usually included with Python on Windows/macOS; Linux often requires installing system package)

**Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-tk
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**macOS**
```bash
# Install Python (if not installed)
brew install python

# Create venv, activate, install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**Windows (PowerShell/Command Prompt)**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
