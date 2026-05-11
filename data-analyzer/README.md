# Data Analyzer

## 项目说明
这是一个使用 Python 和 pandas 编写的学生成绩数据分析小项目。

程序会读取 `students.csv` 文件，并对学生成绩进行基础统计分析。

## 当前功能
- 读取 CSV 文件
- 显示原始数据
- 计算平均分
- 计算最高分
- 计算最低分
- 筛选不及格学生
- 按分数从高到低排序
- matplotlib可视化

## 运行方式

```bash
python main.py
```

## 数据文件
项目使用`students.csv`作为数据来源，包含以下字段：

- `name`：学生姓名
- `score`：学生成绩
- `age`：学生年龄

## 当前学习重点

- 第一次使用 pandas
- 使用`pd.read_csv()`读取 CSV 文件
- 使用 `df["score"]` 读取某一列
- 使用 `mean()、max()、min() `做统计
- 使用条件筛选数据
- 使用 `sort_values() `排序
- 初步理解 CSV 数据分析流程
- 新增柱状图可视化功能
- 使用 plt.bar() 画柱状图
- 使用 plt.axhline() 画平均分基准线
- 通过color把及格和不及格人数分得更清楚