# Python Basic Projects

这是我的 Python 基础阶段项目合集，用来记录从语法、函数、循环、异常处理，到文件读取、API 请求、数据分析和文本处理的练习过程。

这个仓库的重点不是做大型应用，而是把每一个阶段学到的基础能力沉淀成可运行、可复习、可继续迭代的小项目。

## 项目列表

| 项目 | 学习重点 |
| --- | --- |
| `number-analyzer` | 数字统计、循环、异常处理、函数拆分 |
| `student-score-analyzer` | 成绩统计、条件判断、字典返回结果 |
| `data-analyzer` | pandas、CSV 读取、基础统计、matplotlib 可视化 |
| `text-analyzer` | jieba 分词、词频统计、文本可视化 |
| `exchange-rate-checker` | requests、真实 API、JSON 解析、汇率换算 |

## 学习脉络

这些项目大致按学习过程分成三类：

- 基础语法和输入处理：`number-analyzer`、`student-score-analyzer`
- 数据和文本处理：`data-analyzer`、`text-analyzer`
- 外部数据接口：`exchange-rate-checker`

## 运行方式

每个子项目都有自己的 `README.md` 和 `pyproject.toml`。进入对应项目目录后运行：

```bash
uv run main.py
```

## GitHub 维护方式

这个目录对应 GitHub 仓库：`python-basic-projects`。

历史上这些小项目曾经是独立仓库；之后统一收进这个领域仓库，方便按学习阶段维护。每个子项目的具体说明会保留在项目自己的 `README.md` 中。
