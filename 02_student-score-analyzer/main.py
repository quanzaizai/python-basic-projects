"""
💡【知识点】学生成绩统计分析器 (字典容器操作、聚合计算与等级判定)
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. 容器映射：使用字典 (dict) 存储键值对 {"姓名": 分数}。
  2. 聚合统计：利用 sum()、len()、max()、min() 高效计算均值、及格率与极值。
  3. 分支映射：根据分数区间 (90/80/70/60) 实现多级评定。
--------------------------------------------------------------------------------
"""

# ==================== 1. 等级评定函数 ====================

def evaluate_grade(score: float) -> str:
    """根据分数返回对应的成绩等级"""
    if score >= 90: return "优秀 (A)"
    if score >= 80: return "良好 (B)"
    if score >= 70: return "中等 (C)"
    if score >= 60: return "及格 (D)"
    return "不及格 (F)"

# ==================== 2. 主分析统计流程 ====================

def main():
    # 模拟班级成绩字典
    scores = {
        "Alice": 92.5,
        "Bob": 58.0,
        "Charlie": 84.0,
        "David": 76.5,
        "Eva": 45.0,
        "Frank": 88.0
    }

    score_list = list(scores.values())
    total_students = len(score_list)
    avg_score = sum(score_list) / total_students
    passed_count = sum(1 for s in score_list if s >= 60.0)
    pass_rate = (passed_count / total_students) * 100

    print("=== 全班成绩总览 ===")
    for name, score in scores.items():
        print(f"  {name:10}: {score:5.1f} 分 | 等级: {evaluate_grade(score)}")

    print("\n=== 综合统计指标 ===")
    print(f"  • 学生总数: {total_students} 人")
    print(f"  • 平均成绩: {avg_score:.2f} 分")
    print(f"  • 最高分数: {max(score_list):.1f} 分")
    print(f"  • 最低分数: {min(score_list):.1f} 分")
    print(f"  • 及格比例: {pass_rate:.1f}% ({passed_count}/{total_students})")

if __name__ == "__main__":
    main()
