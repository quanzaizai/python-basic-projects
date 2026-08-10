"""
💡【知识点】Pandas 数据分析与 Matplotlib 成绩可视化
--------------------------------------------------------------------------------
📌【概念与本质】
  1. Pandas DataFrame：二维表格型数据结构，支持矢量化统计计算（mean, max, min）与布尔索引过滤。
  2. 条件颜色映射 (Conditional Coloring)：根据分数动态为柱状图赋予颜色（及格蓝色，不及格红色）。
  3. Matplotlib 中文支持：配置 Arial Unicode MS 字体解决 macOS 系统下图表中文乱码问题。

📌【架构与模块分工】
  1. 数据加载与基础统计：read_csv 读取表格，计算均值、极值。
  2. 条件筛选与排序：布尔索引筛选不及格名单，sort_values 降序排列。
  3. 可视化绘制：生成带平均参考线 (axhline) 的多色柱状图。
--------------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import pandas as pd

# ==================== 1. 数据加载与基础统计 ====================

# 加载 CSV 数据集
df = pd.read_csv("students.csv")

print("=== 原始学生成绩数据 ===")
print(df)
print()

# 矢量化聚合统计
print(f"全班平均分: {df['score'].mean():.2f}")
print(f"最高分:     {df['score'].max()}")
print(f"最低分:     {df['score'].min()}")
print()

# ==================== 2. 条件过滤与排序 ====================

# 布尔索引：筛选分数低于 60 分的学生
fail_students = df[df["score"] < 60]
print("=== 不及格学生名单 ===")
print(fail_students)
print()

# 按照分数降序排列 (ascending=False)
sorted_df = df.sort_values(by="score", ascending=False)
print("=== 按分数降序排列 ===")
print(sorted_df)

# ==================== 3. 动态配色与图表可视化 ====================

# 根据及格线动态构建颜色列表 (及格为蓝色，不及格为红色)
colors = ["blue" if score >= 60 else "red" for score in df["score"]]

# 解决 macOS 中文字体显示问题
plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["score"], color=colors, edgecolor="black", alpha=0.8)

# 绘制平均分参考水平线
average_score = df["score"].mean()
plt.axhline(average_score, color="orange", linestyle="--", linewidth=1.5, label=f"平均线 ({average_score:.1f}分)")

plt.title("学生考试成绩分布柱状图", fontsize=14)
plt.xlabel("学生姓名", fontsize=12)
plt.ylabel("分数", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()