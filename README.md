# Python Basic Projects (Python 基础与实用小工具集)

本项目为 Python 基础语法、数据处理、网络请求与数据可视化的实战小工具集合。

---

## ⚡ 快速环境配置

本项目在根目录统一使用 `uv` 管理虚拟环境与依赖：

```bash
# 安装并同步所有依赖
uv sync

# 运行任意小工具（以文本分析器为例）
uv run python 04_text-analyzer/main.py
```

---

## 📚 案例清单与中文导读索引

| 序号与目录 | 中文项目名 | 核心功能与知识点 | 涉及技术栈 | 运行命令 |
| :---: | :--- | :--- | :--- | :--- |
| **`01_number-analyzer/`** | **数字特征分析器** | 数字奇偶性判断、素数检测、因数分解与历史记录写入 | Python 基础语法、循环、文件写入 | `python 01_number-analyzer/main.py` |
| **`02_student-score-analyzer/`** | **学生成绩统计器** | 成绩录入、及格率统计、最高/最低分计算与等级评定 | 列表、字典数据结构、异常处理 | `python 02_student-score-analyzer/main.py` |
| **`03_exchange-rate-checker/`** | **实时汇率查询工具** | 访问开放汇率 API 接口、JSON 响应解析与货币换算 | `requests` 网络请求、REST API 解析 | `python 03_exchange-rate-checker/main.py` |
| **`04_text-analyzer/`** | **中文分词与词频分析器** | 中文文本分词、高频词统计过滤与 Top 10 词频柱状图生成 | `jieba` 分词、`matplotlib` 可视化 | `python 04_text-analyzer/main.py` |
| **`05_data-analyzer/`** | **成绩数据分析与可视化** | CSV 数据加载、矢量化过滤排序与条件配色动态图表 | `pandas` 数据分析、`matplotlib` 配色图表 | `python 05_data-analyzer/main.py` |
