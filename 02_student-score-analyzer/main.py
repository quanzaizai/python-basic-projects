"""
【知识点】学生成绩统计器 (聚合统计与等级评定)
--------------------------------------------------------------------------------
1. 容器操作：使用字典存储学生与成绩映射。
2. 聚合统计：计算平均分、及格率、最高/最低分。
3. 等级评定：根据分数区间 (90/80/70/60) 输出对应等级。
--------------------------------------------------------------------------------
"""

def evaluate_grade(score: float) -> str:
    if score >= 90: return "优秀 (A)"
    if score >= 80: return "良好 (B)"
    if score >= 70: return "中等 (C)"
    if score >= 60: return "及格 (D)"
    return "不及格 (F)"

def main():
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

    print("\n=== 统计指标 ===")
    print(f"学生总数: {total_students} 人")
    print(f"平均成绩: {avg_score:.2f} 分")
    print(f"最高分数: {max(score_list):.1f} 分")
    print(f"最低分数: {min(score_list):.1f} 分")
    print(f"及格率:   {pass_rate:.1f}% ({passed_count}/{total_students})")

if __name__ == "__main__":
    main()
