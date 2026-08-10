"""
💡【知识点】文本词频分析实战练习 (Practice Text Analyzer)
--------------------------------------------------------------------------------
📌【概念与本质】
  1. 词频提取流程：读取文件 -> Jieba 分词 -> 单字清洗 -> Counter 频次排序 -> 图表呈现。
  2. 代码健壮性：修复了原本代码中的拼写错误 (wrods -> words)，增强了展示美观度。
--------------------------------------------------------------------------------
"""

from collections import Counter
import jieba
import matplotlib.pyplot as plt

# ==================== 1. 文件读取与分词清洗 ====================

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = list(jieba.cut(text))
filtered_words = [word for word in words if len(word) > 1]

# ==================== 2. 词频统计 Top-5 ====================

word_counts = Counter(filtered_words)
top5 = word_counts.most_common(5)

print("=== 词频 Top-5 结果 ===")
for rank, (w, c) in enumerate(top5, 1):
    print(f"Top {rank}: {w} ({c} 次)")

word_list = [item[0] for item in top5]
counts_list = [item[1] for item in top5]

# ==================== 3. 绘制统计图 ====================

plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(8, 5))
plt.bar(word_list, counts_list, color="#55A868", edgecolor="black", alpha=0.85)
plt.title("词频分析练习柱状图", fontsize=14)
plt.xlabel("词语", fontsize=12)
plt.ylabel("出现次数", fontsize=12)
plt.tight_layout()
plt.show()