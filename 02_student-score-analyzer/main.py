"""
=============================================================================
💡【知识点】Python 基础实战 —— 学生成绩统计分析器 (Score Analyzer)
=============================================================================

📌【1. 核心功能与 Python 基础概念】
  - 字典数据结构 (dict) : 键值对映射 `{"姓名": 分数}`，支持 $O(1)$ 快速检索。
  - 内置聚合函数 (Built-in Aggregations) : 
    - `sum()` : 累加求和
    - `len()` : 获取样本总人数
    - `max()` / `min()` : 快速获取全班最高/最低分数
  - 列表推导式与生成器表达式 : `sum(1 for s in score_list if s >= 60.0)` 高效统计达标人数。
  - 格式化字符串 (f-string) : 精确控制浮点数保留小数位数 (如 `{avg_score:.2f}`)。

📌【2. 等级评定标准模型】
  - $[90, 100]$ : 优秀 (A)
  - $[80, 90)$  : 良好 (B)
  - $[70, 80)$  : 中等 (C)
  - $[60, 70)$  : 及格 (D)
  - $[0, 60)$   : 不及格 (F)
=============================================================================
"""

# ==================== 0. 类型注解标准模块引入 ====================
from typing import Dict   # 类型提示库：提供 Dict 用于对映射字典与函数参数进行严谨类型注解


# ==================== 1. 业务逻辑函数 ====================

def evaluate_grade(score: float) -> str:
    """
    根据给定的百分制考试分数返回对应的等级描述

    :param score: 浮点型考试成绩 (0 ~ 100)
    :return: 对应的成绩评定等级字符串
    """
    if score >= 90.0:
        return "优秀 (A)"
    elif score >= 80.0:
        return "良好 (B)"
    elif score >= 70.0:
        return "中等 (C)"
    elif score >= 60.0:
        return "及格 (D)"
    else:
        return "不及格 (F) ⚠️"


# ==================== 2. 主分析统计流程 ====================

def main() -> None:
    """成绩分析器主执行流程"""
    # 模拟全班成绩字典数据集
    student_scores: Dict[str, float] = {
        "Alice": 92.5,
        "Bob": 58.0,
        "Charlie": 84.0,
        "David": 76.5,
        "Eva": 45.0,
        "Frank": 88.0
    }

    # 【步骤 1】提取数值列表进行数学聚合计算
    score_list = list(student_scores.values())
    total_students = len(score_list)
    
    if total_students == 0:
        print("⚠️ 成绩库为空，无法进行统计！")
        return

    avg_score = sum(score_list) / total_students
    max_score = max(score_list)
    min_score = min(score_list)

    # 统计及格人数与及格率
    passed_count = sum(1 for s in score_list if s >= 60.0)
    pass_rate = (passed_count / total_students) * 100.0

    # 【步骤 2】格式化输出全员明细清单
    print("=" * 45)
    print("        📋 全班学生成绩明细表        ")
    print("=" * 45)
    for name, score in student_scores.items():
        grade_desc = evaluate_grade(score)
        print(f"  • {name:<10} : {score:5.1f} 分  |  评级: {grade_desc}")

    # 【步骤 3】输出综合宏观统计指标
    print("\n" + "=" * 45)
    print("        📊 综合学术统计指标        ")
    print("=" * 45)
    print(f"  • 参考总人数 : {total_students} 人")
    print(f"  • 全班平均分 : {avg_score:.2f} 分")
    print(f"  • 全班最高分 : {max_score:.1f} 分")
    print(f"  • 全班最低分 : {min_score:.1f} 分")
    print(f"  • 考试及格率 : {pass_rate:.1f}% ({passed_count}/{total_students} 人及格)")
    print("=" * 45)


if __name__ == "__main__":
    main()
