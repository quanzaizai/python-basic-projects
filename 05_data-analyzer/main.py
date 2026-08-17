"""
=============================================================================
💡【知识点】Python 数据分析核心 —— Pandas 表格处理与条件配色可视化
=============================================================================

📌【1. 核心技术栈与数据处理原理】
  - Pandas DataFrame :
    - 二维带行标签和列标签的表格型数据结构。
    - 矢量化运算 (Vectorized Computation) : 内部由 C/Cython 优化，计算 `mean()`, `max()` 比纯 Python 循环快数十倍。
  - 布尔索引过滤 (Boolean Indexing) :
    - `df[df["score"] < 60]` 利用布尔掩码向量一次性筛选出所有不达标样本。
  - Matplotlib 条件动态配色 :
    - 通过列表推导式为达标项赋予沉稳蓝色 (`#2b5c8f`)，为预警项赋予醒目红色 (`#d9534f`)。
    - `plt.axhline()` 叠加全局平均基准线。
=============================================================================
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    """学生成绩数据分析与条件配色可视化"""
    print("=" * 48)
    print("      📊 Pandas 学生成绩综合数据分析工作流      ")
    print("=" * 48)

    # 【步骤 1】准备/加载 CSV 数据文件
    csv_file = Path(__file__).resolve().parent / "students.csv"
    if not csv_file.exists():
        df_init = pd.DataFrame({
            "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
            "score": [92, 58, 84, 76, 45, 88]
        })
        df_init.to_csv(csv_file, index=False)

    df = pd.read_csv(csv_file)

    # 【步骤 2】控制台输出 DataFrame 概览与统计量
    print("\n📋 【数据集原始表格】")
    print(df.to_string(index=False))

    avg_score = df["score"].mean()
    max_score = df["score"].max()
    min_score = df["score"].min()

    print("\n📈 【统计核心指标】")
    print(f"  • 全班平均分: {avg_score:.2f} 分")
    print(f"  • 最高分记录: {max_score} 分 (学生: {df.loc[df['score'].idxmax(), 'name']})")
    print(f"  • 最低分记录: {min_score} 分 (学生: {df.loc[df['score'].idxmin(), 'name']})")

    # 【步骤 3】布尔切片筛选不及格名单
    fail_students = df[df["score"] < 60]
    print("\n⚠️ 【不及格预警名单 (Score < 60)】")
    if not fail_students.empty:
        print(fail_students.to_string(index=False))
    else:
        print("  🎉 全员及格！")

    # 【步骤 4】动态条件配色 Matplotlib 柱状图
    # 列表推导式：及格显示专业蓝，不及格显示告警红
    colors = ["#2b5c8f" if s >= 60 else "#d9534f" for s in df["score"]]

    # 配置中文字体
    plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(8.5, 4.8))
    bars = plt.bar(df["name"], df["score"], color=colors, edgecolor="black", alpha=0.85)

    # 在柱子顶部标注具体数值
    for bar in bars:
        h = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2, 
            h + 1, 
            f"{h}", 
            ha="center", 
            va="bottom", 
            fontsize=10, 
            fontweight="bold"
        )

    # 绘制全班平均水平参考线
    plt.axhline(avg_score, color="#ff7f0e", linestyle="--", linewidth=1.8, label=f"班级平均线 ({avg_score:.1f}分)")

    plt.title("学生成绩分布柱状图 (及格蓝 / 不及格红)", fontsize=14, pad=12)
    plt.xlabel("学生姓名", fontsize=11)
    plt.ylabel("考试分数 (分)", fontsize=11)
    plt.ylim(0, 105)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(loc="upper right")
    plt.tight_layout()

    print("\n📈 正在生成并弹出学生成绩对比图表...")
    plt.show()


if __name__ == "__main__":
    main()
