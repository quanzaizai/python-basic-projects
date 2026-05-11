def parse_numbers():
    raw_text = input("请输入一串数字：")

    if raw_text =='q':
        return 'q'
    
    if raw_text =='h':
        return 'h'
    
    
    if raw_text.strip() == "":
        print("请至少输入一个整数")
        return None
    
    # try:
            parts = raw_text.split()
            numbers =[]
            for text_num in parts:
                numbers.append(int(text_num))
            return numbers
    
    except ValueError:
            print("请输入正确的整数数据")
            return None

        
def analyzer_numbers(numbers):
    total_sum = 0
    total_count = 0
    even_count = 0
    odd_count = 0
    big_count = 0
    big_sum = 0
    average = 0
    for num in numbers:
        total_count += 1
        total_sum += num
        if num % 2 == 0:
            even_count += 1
        if num % 2 != 0:
            odd_count += 1
        if num > 10:
            big_count += 1
            big_sum += num
    average = total_sum / total_count
    return{"total_sum":total_sum,
           "total_count":total_count,
           "even_count":even_count,
           "odd_count":odd_count,
           "big_count":big_count,
           "big_sum":big_sum,
           "average":average
    }

def print_result(numbers, result):
     print(f"总和为:{result['total_sum']}")
     print(f"总数的个数为:{result['total_count']}")
     print(f"偶数个数为:{result['even_count']}")
     print(f"奇数个数为:{result['odd_count']}")
     print(f"大于10的数的总和为:{result['big_sum']}")
     print(f"大于10的数的个数为:{result['big_count']}")
     print(f"这些数的原始列表为:{numbers}")
     print(f"这些数的平均数为:{result['average']}")


def save_result(numbers, result):
    with open("history.txt", "a", encoding="utf-8") as f:
        print(f"原始数字列表为：{numbers}", file=f)
        print(f"所有数的总和为：{result['total_sum']}", file=f)
        print(f"所有数的个数为：{result['total_count']}", file=f)
        print(f"所有偶数的个数为：{result['even_count']}", file=f)
        print(f"所有奇数的个数为：{result['odd_count']}", file=f)
        print(f"大于10的数的个数为：{result['big_count']}", file=f)
        print(f"大于10的数的总和为：{result['big_sum']}", file=f)
        print(f"所有数的平均数为：{result['average']}", file=f)
        print("-" * 30, file=f)


def read_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("当前还没有历史记录")

          
def main():
    while True:
        numbers = parse_numbers()

        if numbers == 'q':
            print("程序结束")
            break

        if numbers == 'h':
            read_history()
            continue

        if numbers is not None:
            result = analyzer_numbers(numbers)
            print_result(numbers, result)
            save_result(numbers, result)


if __name__ == "__main__" :
    main()
