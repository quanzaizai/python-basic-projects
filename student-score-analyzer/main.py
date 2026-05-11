def parse_scores():
    raw_text = input("请输入一串成绩,中间用空格隔开:")

    if raw_text.strip() == "":
        print("请至少输入一个整数")
        return None

    if raw_text.strip() == "q":
        print("程序结束")
        return "q"

    try:
        parts = raw_text.split()
        scores = []

        for n in parts:
            scores.append(int(n))

        return scores
    
    except ValueError:
        print("请输入正确的数字")
        return None

def analyze_scores(scores):

    total_score = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    average_score = total_score / len(scores)

    pass_count = 0
    fail_count = 0
    good_count = 0
    excellent_count = 0

    for score in scores:
        if score < 60:
            fail_count += 1
        elif score < 80:
            pass_count += 1
        elif score < 90:
            good_count += 1
        else:
            excellent_count += 1
    
    return{"total_score":total_score,
           "max_score":max_score,
           "min_score":min_score,
           "average_score":average_score,
           "pass_count":pass_count,
           "fail_count":fail_count,
           "good_count":good_count,
           "excellent_count":excellent_count
           
    }


def print_result(result):

    print(f"总分为:{result['total_score']}")
    print(f"最高分为:{result['max_score']}")
    print(f"最低分为:{result['min_score']}")
    print(f"平均分为:{result['average_score']}")
    print(f"60-79分人数为:{result['pass_count']}")
    print(f"不及格人数为:{result['fail_count']}")
    print(f"良好人数为:{result['good_count']}")
    print(f"优秀人数为:{result['excellent_count']}")
    


def main():
    while True:
        zx_score = parse_scores()

        if zx_score == "q":
            break
        
        if zx_score is not None:
            zx_result = analyze_scores(zx_score)
            print_result(zx_result)

if __name__ == "__main__":
    main()