"""
💡【知识点】学生成绩统计分段模型与控制台 CLI 架构
--------------------------------------------------------------------------------
📌【概念与本质】
  1. 成绩区间分段统计：
     - 不及格 (Fail): < 60 分
     - 及格 (Pass): 60 ~ 79 分
     - 良好 (Good): 80 ~ 89 分
     - 优秀 (Excellent): >= 90 分
  2. 健壮的输入校验：基于 split() 与 list comprehension 处理空格分隔数据。

📌【架构与模块分工】
  1. parse_scores()   : 交互式获取并解析成绩列表，支持 q 退出。
  2. analyze_scores() : 综合计算总分、极值、均值与四大等级段人数分布。
  3. print_result()   : 格式化打印成绩分析报表。
  4. main()           : 循环驱动入口。
--------------------------------------------------------------------------------
"""

# ==================== 1. 成绩输入与解析 ====================

def parse_scores():
    """解析控制台输入的空格分隔分数串，支持 q 退出"""
    raw_text = input("请输入一组学生成绩（空格隔开，输入 q 退出）: ").strip()

    if raw_text.lower() == "q":
        return "q"
    if not raw_text:
        print("【提示】输入不能为空，请至少输入一个有效成绩。\n")
        return None

    try:
        scores = [int(n) for n in raw_text.split()]
        # 成绩合理性校验 (0 ~ 100)
        for s in scores:
            if s < 0 or s > 100:
                print(f"【警告】存在超出 [0, 100] 范围的异常分数: {s}")
        return scores
    except ValueError:
        print("【错误】请输入有效的纯数字成绩！\n")
        return None

# ==================== 2. 成绩分段与指标聚合 ====================

def analyze_scores(scores):
    """统计总分、最高分、最低分、平均分以及各成绩段人数"""
    total_score = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    average_score = total_score / len(scores) if scores else 0.0

    fail_count = 0      # < 60
    pass_count = 0      # 60 ~ 79
    good_count = 0      # 80 ~ 89
    excellent_count = 0 # >= 90

    for score in scores:
        if score < 60:
            fail_count += 1
        elif score < 80:
            pass_count += 1
        elif score < 90:
            good_count += 1
        else:
            excellent_count += 1
    
    return {
        "total_score": total_score,
        "max_score": max_score,
        "min_score": min_score,
        "average_score": average_score,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "good_count": good_count,
        "excellent_count": excellent_count,
        "total_students": len(scores)
    }

# ==================== 3. 报表输出与驱动入口 ====================

def print_result(result):
    """格式化打印成绩分析汇总"""
    print("\n========== 学生成绩统计报表 ==========")
    print(f"参考总人数:       {result['total_students']} 人")
    print(f"全班总分:         {result['total_score']} 分")
    print(f"最高分:           {result['max_score']} 分")
    print(f"最低分:           {result['min_score']} 分")
    print(f"平均分:           {result['average_score']:.2f} 分")
    print("-" * 38)
    print(f"优秀 (90~100分):  {result['excellent_count']} 人")
    print(f"良好 (80~89分):   {result['good_count']} 人")
    print(f"及格 (60~79分):   {result['pass_count']} 人")
    print(f"不及格 (<60分):   {result['fail_count']} 人")
    print("======================================\n")

def main():
    while True:
        scores = parse_scores()
        if scores == "q":
            print("程序已退出。")
            break
        
        if scores is not None:
            result = analyze_scores(scores)
            print_result(result)

if __name__ == "__main__":
    main()