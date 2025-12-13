[![en](https://img.shields.io/badge/lang-en-yellow.svg)](https://github.com/BlanQwall/StepLog/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-green.svg)](https://github.com/BlanQwall/StepLog/blob/main/README.zh-Hans.md)

# StepLog · Berlin 2026 🏃‍♂️

**A data-driven training log toward Berlin Marathon 2026 · Sub-3**

🔗 Live site:  
https://blanqwall.github.io/StepLog/index.html

**Hongkong mirror**: https://cn.steplog.cn

![Berlin 2026](berlin-2026/assets/Berlin_2026_logo_200px.png)
![Berlin-2026-zh Logo](berlin-2026/assets/Berlin_2026_logo-zh_200px.png)
---

## What is StepLog?

**StepLog** is a fully static, automated training-log system documenting a long-term marathon project:

> **Berlin Marathon 2026 · Sub-3 hours**

The project is built around **cycles**, **weekly execution**, and **continuous reflection**, combining structured training plans with real Strava and calendar data.

> **Plan first. Learn from every week. Build Sub-3 with steady steps.**

---

## Key Features

- 📆 **Season-based planning**  
  Multi-cycle roadmap with intermediate races and a final Sub-3 goal.

- 🗓 **Dynamic weekly logs**  
  One template, parameterized by week (`?week=YYYY-MM-DD`), fully static.

- 🚴 **Strava integration**  
  Automatic ingestion of runs, trails, and swims via webhooks.

- 📸 **Weekly photos**  
  Strava activity photos are collected and embedded into weekly logs.

- 📊 **Full-season analytics**  
  Distance, sessions, and effort visualized with Canvas-based charts.

- 🌐 **Bilingual (EN / ZH)**  
  English & Chinese pages rendered from paired JSON datasets.

---

## Automation & Architecture

- **Frontend**: GitHub Pages (HTML / CSS / Vanilla JS)
- **Backend scripts**: Python (cron-driven, private repo)
- **Strava**: Cloudflare Webhook → KV Queue → Ubuntu cron
- **Calendar**: Outlook / Garmin ICS → JSON
- **Translation**: OpenAI API + local translation cache
- **Asia mirror**: Hong Kong deployment + Tencent Cloud Object Storage

All updates are **fully automated**, from activity ingestion to weekly page generation and Git commits.

---

## Philosophy

This is not just a log of workouts.

It is a system designed to answer one question clearly:

> *What am I doing this week — and how does it move me closer to Sub-3 in Berlin 2026?*

---

📖 **Full documentation & technical details**  
→ See the complete README below or explore the live site.
