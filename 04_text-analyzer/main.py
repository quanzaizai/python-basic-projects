"""
💡【知识点】Jieba 中文分词、词频统计 (Counter) 与 Matplotlib 可视化
--------------------------------------------------------------------------------
📌【概念与本质】
  1. Jieba 分词：基于前缀词典实现高效的词图扫描，结合 Viterbi 算法切分中文语句。
  2. 停用与单字过滤：列表推导式 `[w for w in words if len(w) > 1]` 过滤语气词与标点单字。
  3. Counter 聚合：标准库 collections.Counter 高效统计词频，most_common(N) 提取 Top-N 热词。

📌【架构与模块分工】
  1. 文本读取与中文分词：utf-8 编码安全读取文本并调用 jieba.cut。
  2. 词频统计与 Top-N 提取：Counter.most_common(5) 提取高频词。
  3. 柱状图呈现：Matplotlib 绘制词频条形图并配置中文字体。
--------------------------------------------------------------------------------
"""

from collections import Counter
import jieba
import matplotlib.pyplot as plt

# ==================== 1. 文本读取与 Jieba 中文分词 ====================

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 中文精准切词
raw_words = list(jieba.cut(text))

# 过滤长度 <= 1 的单字与标点符号，保留实际词汇
filtered_words = [word for word in raw_words if len(word) > 1]

# ==================== 2. 词频聚合与 Top-5 提取 ====================

word_counts = Counter(filtered_words)
top5 = word_counts.most_common(5)

print("=== 出现频次最高的 Top-5 词汇 ===")
for rank, (word, count) in enumerate(top5, 1):
    print(f"{rank}. 【{word}】: {count} 次")

# 拆分键与值供图表渲染
words_list = [item[0] for item in top5]
counts_list = [item[1] for item in top5]

# ==================== 3. 词频柱状图可视化 ====================

plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(8, 5))
bars = plt.bar(words_list, counts_list, color="#4C72B0", edgecolor="black", alpha=0.85)

# 在柱子上方标注具体频次数值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height + 0.1, f"{int(height)}", ha="center", va="bottom")

plt.title("文本高频词汇 Top-5 统计图", fontsize=14)
plt.xlabel("高频词语", fontsize=12)
plt.ylabel("出现次数", fontsize=12)
plt.tight_layout()
plt.show()