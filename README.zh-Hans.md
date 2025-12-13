[![en](https://img.shields.io/badge/lang-en-yellow.svg)](https://github.com/BlanQwall/StepLog/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-green.svg)](https://github.com/BlanQwall/StepLog/blob/main/README.zh-Hans.md)

# StepLog · Berlin 2026 🏃‍♂️

**一个围绕柏林马拉松 2026 · Sub-3 的数据化训练记录系统**

🔗 在线访问：  
https://blanqwall.github.io/StepLog/index.html
**香港镜像**: https://cn.steplog.cn

![Berlin 2026](berlin-2026/assets/Berlin_2026_logo_200px.png)
![Berlin-2026-zh Logo](berlin-2026/assets/Berlin_2026_logo-zh_200px.png)

---

## StepLog 是什么？

**StepLog** 是一个完全静态、自动化的训练记录系统，用来长期记录并分析一个明确的目标：

> **柏林马拉松 2026 · 三小时内完赛（Sub-3）**

整个项目以 **周期（Cycle）** 和 **周（Week）** 为核心单位，把训练计划、实际执行、数据分析和复盘系统化地组织在一起。

> **计划在前，一周一复盘，脚踏实地走向 Sub-3。**

---

## 核心特性

- 📆 **赛季级训练规划**  
  以多个训练周期构建完整路线图，包含阶段性比赛与最终目标。

- 🗓 **动态周记页面**  
  使用参数化模板（`?week=YYYY-MM-DD`），在纯静态环境中生成每周视图。

- 🚴 **Strava 自动接入**  
  通过 Webhook 自动抓取跑步、越野跑和游泳活动数据。

- 📸 **每周训练照片**  
  自动收集 Strava 活动照片并展示在周记中，让记录不只停留在数字。

- 📊 **赛季全局数据可视化**  
  用原生 Canvas 绘制里程、训练次数、强度变化，直观呈现训练走势。

- 🌐 **中英双语体系**  
  英文 / 中文页面并行，数据结构一致，自动切换语言。

---

## 自动化与技术架构

- **前端**：GitHub Pages（HTML / CSS / 原生 JS）
- **后端脚本**：Python（私有仓库 + cron）
- **Strava 数据流**：  
  Strava → Cloudflare Webhook → KV 队列 → Ubuntu 定时任务
- **日历数据**：Outlook / Garmin ICS → JSON
- **智能翻译**：OpenAI API + 本地翻译缓存
- **亚洲镜像**：香港部署 + 腾讯云对象存储（COS）

从训练完成到周记生成、提交、发布，**全流程自动化**。

---

## 项目理念

这不是一个简单的“跑步记录网站”。

StepLog 关注的是：

> **这一周我做了什么？  
> 它是否让我更接近 2026 年柏林的 Sub-3？**

---

📖 **完整技术说明与设计细节**  
→ 请查看完整 README 或直接访问在线页面
