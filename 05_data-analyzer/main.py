"""
💡【知识点】Pandas 数据分析与 Matplotlib 条件配色可视化
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. Pandas DataFrame：表格型数据结构，支持 read_csv 加载与矢量化统计 (mean/max/min)。
  2. 条件颜色映射：利用列表推导式根据成绩（>=60 蓝色，<60 红色）动态配置图表颜色。
  3. 参考基准线：axhline 绘制全班平均分虚线。
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

    # ==================== 1. 数据加载与基础统计 ====================
    df = pd.read_csv(csv_file)

    print("=== 原始学生成绩表格 ===")
    print(df)
    print(f"\n  • 全班平均分: {df['score'].mean():.2f} 分")
    print(f"  • 全班最高分: {df['score'].max()} 分")
    print(f"  • 全班最低分: {df['score'].min()} 分\n")

    # ==================== 2. 布尔索引筛选 ====================
    fail_students = df[df["score"] < 60]
    print("=== 不及格学生名单 ===")
    print(fail_students)

    # ==================== 3. 动态条件配色柱状图 ====================
    colors = ["#2b5c8f" if s >= 60 else "#d9534f" for s in df["score"]]

    plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(8, 4.5))
    plt.bar(df["name"], df["score"], color=colors, edgecolor="black", alpha=0.85)
    
    # 绘制全班平均分虚线
    avg = df["score"].mean()
    plt.axhline(avg, color="orange", linestyle="--", linewidth=1.5, label=f"平均线 ({avg:.1f}分)")
    
    plt.title("学生成绩分布柱状图 (及格蓝 / 不及格红)", fontsize=14)
    plt.xlabel("学生姓名", fontsize=12)
    plt.ylabel("考试分数", fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
