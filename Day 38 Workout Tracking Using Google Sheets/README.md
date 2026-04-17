# Day 38: Workout Tracking with NLP & Google Sheets

## 🏗️ Project Overview
This project is a sophisticated health management tool that bridges Natural Language Processing (NLP) with automated productivity software. By integrating the **Nutritionix API**, users can input workout data using natural language (e.g., "I swam for 50 mins"). The program automatically parses the exercise type, duration, and calories burned, then synchronizes this data directly into a **Google Sheet**.

## 🛠️ Tech Stack
* **Python**: Core logic and automation.
* **Nutritionix API**: Leverages NLP to interpret workout semantics.
* **Sheety API**: Handles RESTful API requests to bridge Python with Google Sheets.
* **Environment Variables (`.env`)**: Managed via `python-dotenv` to secure sensitive API credentials and enhance portability.
* **Git/GitHub**: Version control with robust `.gitignore` implementation to prevent credential leaks.

## 🌟 Key Features
* **Natural Language Recognition**: Eliminates manual parameter entry; the AI handles the calculations.
* **Automated Logging**: Instant data synchronization—once the workout is entered, it’s in the spreadsheet.
* **Security & Decoupling**: API credentials are fully abstracted from the source code, adhering to industry-standard security practices.

## 🚀 Future Roadmap
* [ ] **Multi-Source Data Fusion**: Integrate **OpenWeather API** to automatically log local Vancouver weather and temperature during workouts.
* [ ] **Vital Sign Interception**: Implement custom logic to capture heart rate, blood pressure, and personal comments.
* [ ] **Data Visualization**: Generate weekly fitness trend reports automatically within Google Sheets.

---
*"Digital Craftsmanship: Refactoring health management through code."*




# Day 38: Workout Tracking with NLP & Google Sheets

## 🏗️ 项目概述 (Project Overview)
这是一个将自然语言处理（NLP）与自动化办公工具结合的健康管理项目。通过接入 Nutritionix API，用户可以用自然的口语（如 "I ran for 30 mins"）输入运动数据，程序会自动解析运动类型、时长及消耗的卡路里，并同步记录到 Google Sheets 中。

## 🛠️ 技术栈 (Tech Stack)
* **Python**: 核心逻辑编写。
* **Nutritionix API**: 利用 NLP 技术解析运动语义。
* **Sheety API**: 将数据通过 RESTful API 传输至 Google Sheets。
* **Environment Variables (`.env`)**: 使用 `python-dotenv` 管理敏感 API 秘钥，确保代码安全性与可移植性。
* **Git/GitHub**: 版本控制与代码托管，实践了 `.gitignore` 安全防护规范。

## 🌟 核心功能 (Key Features)
* **自然语言识别**: 无需手动输入复杂参数，AI 自动计算运动指标。
* **自动化记账**: 运动完成即入表，实现数据无感同步。
* **安全解耦**: 所有的 API 凭据均已从主代码中抽离，遵循工业级安全标准。

## 🚀 未来计划 (Future Roadmap)
* [ ] **多源数据融合**: 接入 OpenWeather API，自动记录运动时的温哥华本地天气与温度。
* [ ] **体征截留逻辑**: 增加对心率、血压及个人感受（Comments）的自定义解析。
* [ ] **数据可视化**: 基于 Google Sheets 自动生成每周运动趋势报表。

---
*“数字化木工：用代码重构健康管理逻辑。”*
