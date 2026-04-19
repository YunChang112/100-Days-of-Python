# 📝 Python Day 22: The Pong Game - "Digital Craftsmanship"

## 🇨🇳 中文版：数字手艺人的觉醒

### 🛠️ 项目复盘
在第 22 天，我利用 Python 的 `turtle` 库从零构建了经典的 **Pong** 游戏。通过这个项目，我不仅完成了代码的堆砌，更完成了一次从“手动操作”到“系统调度”的思维跃迁。

### 💡 核心学习与技术实现
* **面向对象编程 (OOP) 的力量**：
    * **封装 (Encapsulation)**：我将球拍、球、计分板分别独立成类。`main.py` 不再关心细节，只负责“指挥”。
    * **类与实例 (Class & Instance)**：只编写了一个 `Paddle` 类，通过传入不同的坐标和颜色参数，轻松创建了左右两个独立运行的球拍。
* **物理逻辑控制**：
    * 引入了 **Vector Movement (向量移动)**：使用 `x_move` 和 `y_move` 代替固定坐标。
    * **碰撞反弹**：理解了反弹的本质是向量取反（$y\_move \cdot -1$ 或 $x\_move \cdot -1$）。
* **游戏平衡算法**：
    * 通过 `self.move_speed *= 0.9` 实现了击球加速逻辑，让游戏具备了挑战性和动态美感。

### 🌟 顿悟与进步
> **“对话变少了，是因为思维变深了。”**

作为一名深耕现场十年的红印章木工（Red Seal Carpenter），我发现代码也是一种“手艺”：
* **预制思维**：类就像是我的木工模具，实例则是产出的标准化零件。
* **数字解耦**：就像建筑结构中承重墙与装饰层的分离，OOP 让我的代码结构清晰、互不干扰。
* **进步标志**：我不再卡在“怎么画图”上，而是开始思考“如何建立规则”。我感受到了从“使用者”向“创造者”的转变。

---

## 🇺🇸 English Version: The Awakening of a Digital Craftsman

### 🛠️ Project Overview
On Day 22, I built the classic **Pong Game** from scratch using the Python `turtle` library. This project was more than just writing code; it was a transition from "manual operation" to "system orchestration."

### 💡 Key Learning & Technical Implementation
* **The Power of OOP**:
    * **Encapsulation**: I decoupled the Paddles, Ball, and Scoreboard into independent classes. `main.py` no longer handles details; it acts as the project manager.
    * **Class & Instance**: I wrote a single `Paddle` class and created two distinct paddles (left and right) by passing different coordinates and colors.
* **Physics Logic Control**:
    * **Vector Movement**: Implemented `x_move` and `y_move` instead of hard-coded coordinates.
    * **Reflection Logic**: Grasped that bouncing is essentially inverting the movement vector ($y\_move \cdot -1$ or $x\_move \cdot -1$).
* **Game Balancing Algorithm**:
    * Implemented `self.move_speed *= 0.9` to increase the ball's speed after each hit, adding dynamic difficulty to the game.

### 🌟 Epiphanies & Progress
> **"Fewer questions, deeper thoughts."**

As a Red Seal Carpenter with ten years of field experience, I’ve realized that coding is a form of "Digital Craftsmanship":
* **Prefabrication Mindset**: Classes are like my carpentry jigs/templates, and instances are the standardized components produced from them.
* **Digital Decoupling**: Just like separating structural framing from interior finishing in a building, OOP keeps my code organized and modular.
* **Signs of Growth**: I am no longer stuck on "how to draw"; I am now focusing on "how to build the rules." This marks my evolution from a "user" to a "creator."

---

### 🚀 Technical Stack
`Python 3.x` | `Turtle Graphics` | `OOP` | `Logic Algorithms`