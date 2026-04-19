# Python Day 17: Quiz Project & OOP Logic Evolution 🚀

## 📌 Project Overview
This project is part of Day 17 of the "100 Days of Code" Python challenge. By building an automated quiz application, I explored the core principles of **Object-Oriented Programming (OOP)**. The focus was on transitioning from "Procedural Coding" to "High-level Architecture."

## 🧠 Learning Journey & Key Insights

### 1. From "Manual Middleman" to "Logical Automaton"
* **Phase 1**: Initially, I acted as a middleman in `main.py`, manually extracting user input and passing it back to `check_answer`. 
* **The Epiphany**: I realized the power of the **"Tell, Don't Ask"** principle. By calling `check_answer()` internally within `next_question()`, the main program only needs to issue the start command. The subsequent causal chain is triggered automatically inside the object.

### 2. The Power of Modularity
* By integrating the **Open Trivia DB API**, I experienced the strength of data decoupling.
* **Core Concept**: As long as the `QuizBrain` class is robust, the core logic remains untouched even when external data keys change (e.g., from `text` to `question`). We only need to adapt at the entry point.

### 3. BIM (Building Information Modeling) Industry Mapping
I successfully mapped these OOP principles to Revit and Dynamo development:
* **Revit API = Data Source**: Elements (walls, beams, slabs) retrieved via API are instances of objects with specific attributes.
* **OOP Auditing**: Transformed the quiz logic into a `ConstructionManager` class. Elements are no longer static models but "intelligent objects" with built-in logic for quantity takeoff, clash detection, and site layout.

## 🛠️ Key Bug Fixes
* **Dictionary Iteration**: Corrected the misconception that `for item in dict` iterates through values (it iterates through keys by default).
* **'Object' not subscriptable**: Clarified the boundary between Objects and Lists, learning to access nested data via the `.attribute` path.
* **Attribute Timing**: Resolved the `self.question_number - 1` offset issue to ensure scores are accurately mapped to the current question.

## 💡 Mentor's Reflection
> "Code is not just a set of instructions; it is a lens through which we observe and define the rules of the universe and construction."




# Python Day 17: Quiz 项目与 OOP 逻辑演进 🚀

## 📌 项目简介
本项目是 Python "100 Days of Code" 系列的第 17 天。通过构建一个自动化测验程序，深入探索了 **面向对象编程 (OOP)** 的核心原则。本项目不仅实现了功能，更重要的是完成了一次从“过程式代码”到“高阶架构”的思维跃迁。

## 🧠 学习历程与核心顿悟

### 1. 从“手动搬运”到“逻辑自动机”
* **最初阶段**：我在 `main.py` 里手动提取用户输入，再作为传参送回 `check_answer`。这是一种典型的“中间人”思维。
* **顿悟时刻**：通过对标标准答案，我发现高阶架构应遵循 **"Tell, Don't Ask"（下令，而非询问）** 原则。在 `next_question()` 内部直接调用 `check_answer()`，主程序只需下达起始指令，后续的因果链条在对象内部自动触发。

### 2. 模块化（Modularity）的降维打击
* 通过接入 **Open Trivia DB API**，我深刻体会到了数据解耦的力量。
* **核心逻辑**：只要 `QuizBrain` 类设计得足够稳健，无论外部数据键名如何变（从 `text` 变成 `question`），只需在入口处做微调，核心“大脑”无需改动一行代码。

### 3. BIM (建筑信息模型) 行业实战映射
我将这一逻辑成功跨界应用到了 Revit 和 Dynamo 开发思维中：
* **Revit API = 数据源**：通过 API 抓取的构件（墙、梁、板）就是带属性的对象实例。
* **OOP 审计**：将 `QuizBrain` 的逻辑转变为 `ConstructionManager` 类。构件不再是死模型，而是自带“审计逻辑”的智能对象，可自动进行算量、碰撞检查及定点放线。

## 🛠️ 典型 Bug 修复记录
* **字典遍历陷阱**：纠正了 `for item in dict` 默认遍历键（Key）而非值（Value）的误区。
* **'Object' not subscriptable**：厘清了 Object 与 List 的边界，学会了通过 `.attribute` 路径访问深层数据。
* **属性调用时序**：解决了 `self.question_number - 1` 的偏移量问题，确保在计分时能精准对应当前题目。

## 💡 导师寄语
> “代码不仅是指令，更是我们观察宇宙与建筑施工规则的显微镜。”