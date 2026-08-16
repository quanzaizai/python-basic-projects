"""
【知识点】Pandas 数据分析与 Matplotlib 可视化
--------------------------------------------------------------------------------
1. Pandas DataFrame：表格数据加载 (read_csv) 与矢量化统计 (mean/max/min)。
2. 布尔索引：筛选不及格名单与排序 (sort_values)。
3. 条件配色可视化：根据及格线赋予柱状图不同颜色 (及格蓝/不及格红)。
--------------------------------------------------------------------------------
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def main():
    csv_file = Path(__file__).resolve().parent / "students.csv"
    if not csv_file.exists():
        df_init = pd.DataFrame({
            "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
            "score": [92, 58, 84, 76, 45, 88]
        })
        df_init.to_csv(csv_file, index=False)

    df = pd.read_csv(csv_file)

    print("=== 原始成绩数据 ===")
    print(df)
    print(f"\n全班平均分: {df['score'].mean():.2f}")
    print(f"最高分:     {df['score'].max()}")
    print(f"最低分:     {df['score'].min()}\n")

    # 筛选与排序
    fail_students = df[df["score"] < 60]
    print("=== 不及格学生名单 ===")
    print(fail_students)

    # 可视化柱状图
    colors = ["#2b5c8f" if s >= 60 else "#d9534f" for s in df["score"]]
    plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(8, 4.5))
    plt.bar(df["name"], df["score"], color=colors, edgecolor="black", alpha=0.85)
    plt.axhline(df["score"].mean(), color="orange", linestyle="--", label=f"平均线 ({df['score'].mean():.1f}分)")
    plt.title("学生成绩分布柱状图 (及格蓝 / 不及格红)")
    plt.xlabel("姓名")
    plt.ylabel("分数")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
