import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("原始数据：")
print(df)

print(f"平均分为：{df['score'].mean()}")
print(f"最高分为：{df['score'].max()}")
print(f"最低分为：{df['score'].min()}")

fail_students = df[df["score"] < 60]
print("不及格学生：",fail_students)

sorted_df = df.sort_values(by="score", ascending=False)
print("按分数从高到低排序：",sorted_df)

colors = []
for score in df["score"]:
    if score >= 60:
        colors.append("blue")
    else:
        colors.append("red")


plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False
plt.bar(df["name"], df["score"], color=colors)
plt.title("学生成绩柱状图")
plt.xlabel("姓名")
plt.ylabel("分数")
average = df["score"].mean()
plt.axhline(average)
plt.show()