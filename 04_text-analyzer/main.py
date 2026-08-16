"""
💡【知识点】中文文本分词与高频词可视化 (jieba + matplotlib)
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. 中文分词机制：jieba.cut 利用前缀词典与 HMM 隐马尔可夫模型精准切分中文词语。
  2. 词频统计：使用 collections.Counter 快速汇总词频并提取 Top 10。
  3. 中文字体配置：设置 Arial Unicode MS 解决图表中文方块乱码。
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

    # ==================== 1. 中文分词与停用词过滤 ====================
    # 过滤掉单字和空白标点
    words = [w for w in jieba.cut(text) if len(w.strip()) > 1]
    counter = Counter(words)
    top10 = counter.most_common(10)

    print("=== 词频 Top 10 榜单 ===")
    for word, count in top10:
        print(f"  {word:10}: {count} 次")

    # ==================== 2. Matplotlib 图表绘制 ====================
    if top10:
        words, counts = zip(*top10)
        
        # 解决 macOS 中文字体显示问题
        plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
        plt.rcParams["axes.unicode_minus"] = False

        plt.figure(figsize=(8, 4.5))
        plt.bar(words, counts, color="#008080", edgecolor="black", alpha=0.85)
        plt.title("中文高频词分布柱状图", fontsize=14)
        plt.xlabel("词汇", fontsize=12)
        plt.ylabel("出现频次", fontsize=12)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
