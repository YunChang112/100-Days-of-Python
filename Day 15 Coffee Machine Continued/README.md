# ☕ Python Coffee Machine Simulator

A robust, interactive command-line coffee machine application built with Python. This project is part of the **Angela Yu "100 Days of Code"** challenge, focusing on dictionary manipulation, functional modularity, and system logic design.

## 🌟 Project Features

- **Decoupled Architecture**: Independent functions for resource checking, coin processing, transaction validation, and drink making.
- **Data-Driven Units**: Implements a `units` dictionary to dynamically manage measurement units (ml, g), enhancing scalability.
- **Robustness**: Uses a "Gating Mechanism" to ensure all conditions are met before modifying any global state.

## 🛠️ Core Logic Breakdown

### Resource Sufficiency (The Guard Clause)
The system iterates through the **recipe's ingredients** rather than the inventory. This ensures that ingredients not present in a specific recipe (e.g., milk in an Espresso) are gracefully ignored, preventing `KeyError`.



### The Transaction Waterfall
1. **Input**: Capture user choice and coin counts.
2. **Validation**: Check if `resources` can satisfy the `MENU` requirements.
3. **Accounting**: Calculate total value and verify against the price.
4. **Execution**: Provide change, update `profit`, and finally deduct `resources`.

## 🧠 Learning Evolution

Through this project, I evolved my programming mental models:
- **Black Box Thinking**: Defining a function's I/O (Input/Output) before writing internal implementation.
- **Query vs. Command**: Separating "Boolean Queries" (Does it work?) from "Action Commands" (Execute the change).
- **Top-Down Design**: Writing the main controller logic first and letting the high-level needs dictate the creation of sub-functions.

## 🚀 Getting Started

1. Ensure Python 3.x is installed.
2. Run the script: `python coffee_machine.py`.
3. Commands:
   - `espresso / latte / cappuccino`: Make a selection.
   - `report`: View current inventory and total earnings.
   - `off`: Power down the machine.

---



# ☕ Python 咖啡机模拟专家系统

这是一个基于 Python 的互动式咖啡机程序。本项目是 Angela Yu 的 "100 Days of Code" 中的经典挑战，旨在练习 Python 字典的操作、函数的模块化设计以及复杂的业务逻辑处理。

## 🌟 项目亮点

- **模块化架构**：将“资源检查”、“金币处理”、“交易验证”和“咖啡制作”拆分为独立的函数，符合单一职责原则（SRP）。
- **动态数据驱动**：使用 `units` 字典动态管理不同材料的单位（ml, g），提高代码的可维护性。
- **防御性编程**：在扣除资源前进行全量校验，确保系统状态的完整性。

## 🛠️ 核心逻辑说明

### 资源校验 (The Gating Logic)
系统采用“一票否决制”。通过遍历**配方字典**而非库存字典，完美避开了不同咖啡配方（如 Espresso 没有牛奶）导致的 `KeyError`。



### 交易流程
遵循工业级交易安全逻辑：
1. **输入阶段**：获取用户选择及投入的硬币。
2. **校验阶段**：对比所需资源与当前库存。
3. **金币处理**：计算总额并判断是否足以支付。
4. **执行阶段**：找零、更新利润并最终扣除资源。

## 🧠 学习思维进阶 (Learning Insights)

在开发本项目过程中，我完成了以下思维跨越：
- **黑盒思维**：学会了在编写函数前先定义其输入（参数）和输出（返回值）。
- **读写分离**：将只读的“问句型”判断（True/False）与具有副作用的“动词型”动作分离。
- **自顶向下设计**：先构建主循环（Main Loop）的需求，再通过需求“召唤”函数的创建。

## 🚀 快速开始

1. 确保安装了 Python 3.x。
2. 运行脚本：`python coffee_machine.py`。
3. 输入命令：
   - `espresso / latte / cappuccino`: 点单
   - `report`: 查看当前资源库存及盈利
   - `off`: 关闭机器

---