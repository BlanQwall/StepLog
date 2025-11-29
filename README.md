# **StepLog · Berlin 2026 — README**

## 🏃‍♂️ Overview  
**StepLog** is a data-driven, fully static training-log system designed to document the journey toward **Berlin Marathon 2026 · Sub-3**.  
It combines GitHub Pages (frontend), Python automation (backend scripts), Strava integration, calendar parsing, bilingual pages, and dynamic week rendering.

The philosophy of the project:

> **Plan first. Learn from every week. Build Sub-3 with steady steps.**

StepLog tracks all training cycles, weekly logs, historical data, Strava metrics, and event schedules from 2025 to September 2026.

---

# ⚙️ Technology Stack

## **1. GitHub Pages (static frontend)**
The entire site runs without a backend.  
Built using:

- **Pure HTML + CSS**
- **Native JavaScript**
- **Canvas API for charts**
- **No frameworks**, for clarity and full control.

---

## **2. Dynamic Weekly Pages (template-based)**

Instead of generating one HTML file per week, StepLog uses a parameterized template:
```
week-berlin.html?week=YYYY-MM-DD
week-berlin-zh.html?week=YYYY-MM-DD
```
The page:

1. Reads the week start date from the URL  
2. Loads the corresponding JSON data  
3. Renders the week view dynamically  

This reduces duplication and works perfectly in a static hosting environment.

---

## **3. Season Plan (Berlin 2026)**

The season page is fully data-driven, featuring:

### ✔ Timeline bar  
- Represents all weeks from Cycle 1 to Final Cycle  
- Colored cycle segments  
- Weekly tick marks  
- Arrow indicating the current week

### ✔ Collapsible Cycles Table  
- Each row represents a training cycle  
- Expands to show weekly details  
- Highlights current cycle and current week

### ✔ Full-season line chart  
- Distance (km)  
- Sessions (count)  
- Avg effort (Strava Suffer Score)  
- Vertical dashed lines marking cycle boundaries  
- X-axis labeled using “Week # within cycle”  
- Cycle labels (“C1, C2, … Final”) centered under the axis  
- Colored legend matching cycle pages

Rendered entirely with the **Canvas API**.

---

# ⚙️ Automation Pipeline (Private Repository)

All backend scripts run on a personal Ubuntu machine:
`GitHub/Private`
Managed via cron jobs, including Strava ingestion, week building, calendar syncing, and auto-commits.

---

# 🚴 Strava Integration  
### Architecture:
```
Strava → Cloudflare Webhook → KV Queue → Ubuntu Cron → fetch_strava.py → build_week.py
```
### Benefits:
- No exposure of home IP  
- Immediate, event-driven updates  
- Cloudflare KV serves as a lightweight queue  
- Ubuntu pulls new activity IDs and processes them every 10 minutes  

Supported activities:

- Run  
- Trail Run  
- Swim  

---

# 📥 Activity Processing (fetch_strava.py)

Features:

- OAuth token auto-refresh  
- Fetches full activity details  
- Writes to:
  - `strava-history.json`
  - `strava-latest.json`
- Filters unsupported activity types  
- Ensures historical ordering

---

# 📅 Weekly Builder (build_week.py)

Generates weekly summaries:

- Total distance  
- Number of sessions  
- Average suffer score  
- Full activity details  

### Bilingual Output:

- `week-YYYY-MM-DD.json`  
- `week-YYYY-MM-DD.zh.json`

### Smart Translation Cache:

A `translation_cache.json` file stores:

- Previously translated names  
- City/state/country strings  
- Workout terms  
- Common Strava phrases  

Reduces cost and keeps translations consistent.

---

# 📆 Calendar Integration

`fetch_calendar.py`:

- Downloads and validates Outlook ICS files  
- Parses events into JSON  
- Generates bilingual outputs  
- Handles HTML-response errors gracefully  
- Syncs race weeks into StepLog timelines

---

# 🗓 Auto-Generate Weekly Pages

Every Sunday at **08:00**, StepLog:

- Creates EN and ZH week pages  
- Updates JSON files  
- Auto-commits changes  
- Pushes to GitHub → GitHub Pages redeploys automatically

---

# 🔄 Git Auto Sync

A dedicated script:`steplog_git_sync.sh`

Automatically:

- Detects changes  
- Adds files  
- Commits with standard messages  
- Pushes to GitHub  

Untracked files are ignored to avoid noise commits.

---

# 🌐 Bilingual Architecture

Principles:

- Separate EN and ZH templates  
- Data stored in paired `.json` and `.zh.json` versions  
- Rendering logic identical  
- Translation cached locally  
- Future support: browser-based auto language detection

---

# 🎨 Visual Design

Primary color:

- **Berlin Blue: `#0057aa`**

Design goals:

- Minimal, steady, clean  
- Strong hierarchy (season → cycles → weeks → activities)  
- Uncluttered layout  
- Responsive (max-width: 1200px)  
- Unified color system across:
  - Timeline
  - Cycles table
  - Line charts
  - Weekly views

Berlin 2026 logo is integrated into the season header.


---

# 🛠 Local Development

To serve locally:

```bash
cd StepLog
python3 -m http.server http://localhost:8000
```
