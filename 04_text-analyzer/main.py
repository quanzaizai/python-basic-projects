"""
=============================================================================
💡【知识点】Python 文本与可视化 —— 中文分词与高频词频统计图 (Text Analyzer)
=============================================================================

📌【1. 核心技术栈与原理】
  - 中文分词 (jieba) :
    - 中文词语之间没有空格分隔。jieba 采用基于前缀词典构建有向无环图 (DAG)，
      结合动态规划查找最大概率路径，并利用 HMM (隐马尔可夫模型) 处理未登录新词。
  - 高频词频统计 (collections.Counter) :
    - 专用于计数的哈希映射容器，`counter.most_common(N)` 可极速提取出现频次最高的前 N 项。
  - 跨平台图表可视化 (matplotlib) :
    - 解决 macOS / Linux / Windows 跨平台中文方块乱码：配置 `font.family = ["Arial Unicode MS", "SimHei", "sans-serif"]`。
=============================================================================
"""

# ==================== 0. 文本处理、分词与可视化库引入 ====================
from collections import Counter   # 高性能容器库：提供 Counter 快速统计高频词频并提取 Top K
from pathlib import Path          # 面向对象路径管理库：提供跨平台安全文件读写与路径解析
import jieba                      # 结巴分词库：基于前缀词典与 HMM 模型实现中文精准分词
import matplotlib.pyplot as plt   # 数据可视化库：提供柱状图绘制、文本标注与中文字体渲染支持


def main() -> None:
    """中文文本分词与柱状图可视化主程序"""
    print("=" * 45)
    print("       📝 中文文本分词与词频分析可视化       ")
    print("=" * 45)

    # 【步骤 1】自动检测并准备样本语料文件
    sample_file = Path(__file__).resolve().parent / "sample.txt"
    if not sample_file.exists():
        default_content = (
            "Python 是一门优秀的编程语言。Python 语法简洁优美、简单易学，"
            "在数据科学、数据分析、机器学习与人工智能领域应用极为广泛。"
            "学习 Python 和算法不仅充满乐趣，而且能极大提升程序员的逻辑思维能力！"
        )
        sample_file.write_text(default_content, encoding="utf-8")

    text = sample_file.read_text(encoding="utf-8")
    print(f"📖 已成功读取语料样本 (共 {len(text)} 个字符)\n")

    # 【步骤 2】中文精准分词并过滤停用标点与单字
    # 列表推导式：过滤掉长度 <= 1 的无意义助词与标点符号
    words = [w for w in jieba.cut(text) if len(w.strip()) > 1]

    # 【步骤 3】使用 Counter 统计频次并提取 Top 10
    counter = Counter(words)
    top10 = counter.most_common(10)

    print("📊 高频词汇排行榜 Top 10:")
    print("-" * 35)
    for rank, (word, count) in enumerate(top10, 1):
        print(f"  第 {rank:2d} 名 : {word:<10} (频次: {count} 次)")
    print("-" * 35)

    # 【步骤 4】Matplotlib 柱状图绘制
    if top10:
        words_list, counts_list = zip(*top10)

        # 解决中文字体乱码
        plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
        plt.rcParams["axes.unicode_minus"] = False

        plt.figure(figsize=(8.5, 4.5))
        bars = plt.bar(words_list, counts_list, color="#008080", edgecolor="black", alpha=0.85)

        # 在每个柱子上方添加具体的数字标注
        for bar in bars:
            height = bar.get_height()
            plt.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold"
            )

        plt.title("中文文本高频词频分布直方图", fontsize=14, pad=12)
        plt.xlabel("词汇名称", fontsize=11)
        plt.ylabel("出现频次 (次)", fontsize=11)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

        print("\n📈 正在生成并弹出可视化柱状图...")
        plt.show()


if __name__ == "__main__":
    main()
