"""
【知识点】中文文本分词与高频词可视化 (jieba + matplotlib)
--------------------------------------------------------------------------------
1. jieba 分词：使用精准模式 cut 提取中文词汇。
2. 词频统计：使用 collections.Counter 统计 Top 10 高频词。
3. 可视化：生成中文柱状图展示词频分布。
--------------------------------------------------------------------------------
"""

from collections import Counter
from pathlib import Path
import jieba
import matplotlib.pyplot as plt

def main():
    sample_file = Path(__file__).resolve().parent / "sample.txt"
    if not sample_file.exists():
        sample_file.write_text("Python 是一门优秀的编程语言。Python 简单易学，在数据分析与人工智能领域应用广泛。学习 Python 非常有趣！", encoding="utf-8")

    text = sample_file.read_text(encoding="utf-8")

    # 1. 中文分词与停用词过滤 (过滤单字与标点)
    words = [w for w in jieba.cut(text) if len(w.strip()) > 1]
    counter = Counter(words)
    top10 = counter.most_common(10)

    print("=== 词频 Top 10 ===")
    for word, count in top10:
        print(f"  {word}: {count} 次")

    # 2. 绘制词频柱状图
    if top10:
        words, counts = zip(*top10)
        plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
        plt.rcParams["axes.unicode_minus"] = False

        plt.figure(figsize=(8, 4.5))
        plt.bar(words, counts, color="teal", edgecolor="black")
        plt.title("高频词分布柱状图")
        plt.xlabel("词汇")
        plt.ylabel("频次")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
