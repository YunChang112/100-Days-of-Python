import os

# Define the content for the markdown file
md_content = """# Day 24: Mail Merge Automation Project

## 📝 学习笔记与思维突破 | Learning Notes & Breakthroughs

### 1. 路径的真相 (The Reality of Paths)
* **顿悟 (Insight):** 最初纠结于 `../` 无法找到文件，后来意识到在 PyCharm 中，**相对路径的起点是项目根目录**。
* **进步 (Progress):** 不再盲目尝试，学会了站在“根目录大门口”去定位内部文件。
* **Thinking:** In PyCharm, relative paths start from the **Project Root**, not the script's location. Understanding this "Reference Point" is like setting a benchmark on a construction site.

### 2. “在哪里编辑”的困惑 (Where to Edit?)
* **顿悟 (Insight):** 刚开始卡在“如何在文件中直接编辑”，后来通过 `type()` 侦察发现，将文件读取为 **String (字符串)** 就像拿到了一块完整的“布料”。
* **进步 (Progress):** 学会了先读取模板，在内存中完成替换，再写入新文件。
* **Thinking:** I realized I shouldn't try to edit the file itself. Instead, read it into memory as a giant string, manipulate it, and then write the final product.

### 3. 数据清洗：洗名字 (Data Cleaning: Stripping)
* **顿悟 (Insight):** 意识到 `readlines()` 拿到的数据带有不可见的“毛刺”（`\\n` 换行符），如果不洗干净，文件名和内容都会乱套。
* **进步 (Progress):** 掌握了 `.strip()` 的用法，并建立了“拿数据 -> 洗数据 -> 存数据”的自动化流水线意识。
* **Thinking:** Raw data is like rough lumber—it needs "stripping" (sanding) to remove invisible newlines (`\\n`) before it can be used in a clean build.

### 4. 动态生成与基准点 (Dynamic Generation & Reference Points)
* **顿悟 (Insight):** 使用 `f-string` 像插榫卯一样动态生成文件名。同时意识到必须保持模板 `content` 变量的纯洁，每一封信都要基于这个“母模”去复制，避免“基准点偏离”。
* **进步 (Progress):** 从最初的双循环（洗数据+写信）进化到合二为一的高效流水线代码。
* **Thinking:** Using `f-strings` for dynamic filenames and ensuring the original template remains unchanged for each iteration, ensuring every letter starts from the same "master template."

---

## 💻 最终代码实现 | Final Code Implementation

```python
# Master Template Path
with open("Input/Letters/starting_letter.txt") as f:
    content = f.read()

# Read, Clean, and Process Names in one flow
with open("Input/Names/invited_names.txt") as f:
    invited_names = f.readlines()
    for name in invited_names:
        clean_name = name.strip() # Cleaning the "burrs" (newlines)
        
        # Replace placeholders using chained methods
        final_letter = content.replace("[name]", clean_name).replace("Angela", "Yun")
        
        # Dynamic filename generation with f-string
        with open(f"Output/ReadyToSend/letter_to_{clean_name}.txt", "w") as f:
            f.write(final_letter)