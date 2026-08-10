"""
💡【知识点】控制台交互、数值统计分析与文件持久化 (I/O)
--------------------------------------------------------------------------------
📌【概念与本质】
  1. 字符串解析与异常保护：使用 split() 分割空白字符，结合 try-except 处理非整数异常。
  2. 聚合统计模型：单次线性遍历同时计算总和、计数、奇偶分类、阈值过滤 (>10) 与平均值。
  3. 持久化存储 (Persistence)：使用 with open(..., "a") 追加模式将分析历史记录落盘。

📌【架构与模块分工】
  1. parse_numbers()     : 控制台输入解析、指令分流 (q/h) 与类型转换。
  2. analyzer_numbers()  : 核心数值特征统计与指标打包。
  3. print_result()      : 控制台格式化报表呈现。
  4. save_result() / read_history() : 文件持久化存取闭环。
  5. main()              : 交互循环主调度。
--------------------------------------------------------------------------------
"""

# ==================== 1. 输入解析与校验 ====================

def parse_numbers():
    """解析控制台输入的空格分隔数字串，支持 q(退出) 与 h(历史) 快捷指令"""
    raw_text = input("请输入一组整数（空格分隔，输入 h 查历史，q 退出）: ").strip()

    if raw_text.lower() == 'q':
        return 'q'
    if raw_text.lower() == 'h':
        return 'h'
    if not raw_text:
        print("【提示】输入不能为空，请至少输入一个整数。\n")
        return None

    try:
        # 分割并转换为整数列表
        return [int(item) for item in raw_text.split()]
    except ValueError:
        print("【错误】包含非整数内容，请重新输入！\n")
        return None

# ==================== 2. 核心数据特征分析 ====================

def analyzer_numbers(numbers):
    """对传入的整数列表进行全方位统计分析并返回指标字典"""
    total_sum = sum(numbers)
    total_count = len(numbers)
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = total_count - even_count
    
    big_numbers = [n for n in numbers if n > 10]
    big_count = len(big_numbers)
    big_sum = sum(big_numbers)
    average = total_sum / total_count if total_count > 0 else 0.0

    return {
        "total_sum": total_sum,
        "total_count": total_count,
        "even_count": even_count,
        "odd_count": odd_count,
        "big_count": big_count,
        "big_sum": big_sum,
        "average": average
    }

# ==================== 3. 结果呈现与持久化 ====================

def print_result(numbers, result):
    """格式化打印分析报表"""
    print("\n========== 数字分析报表 ==========")
    print(f"原始数字序列:   {numbers}")
    print(f"数字总个数:     {result['total_count']}")
    print(f"所有数字之和:   {result['total_sum']}")
    print(f"所有数字平均值: {result['average']:.2f}")
    print(f"偶数个数:       {result['even_count']}")
    print(f"奇数个数:       {result['odd_count']}")
    print(f"大于10的个数:   {result['big_count']} (其累加和: {result['big_sum']})")
    print("==================================\n")

def save_result(numbers, result):
    """将分析报表追加写入 history.txt 文件中"""
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"原始数字序列: {numbers}\n")
        f.write(f"总个数: {result['total_count']} | 总和: {result['total_sum']} | 平均值: {result['average']:.2f}\n")
        f.write(f"偶数: {result['even_count']} | 奇数: {result['odd_count']} | 大于10: {result['big_count']}\n")
        f.write("-" * 40 + "\n")

def read_history():
    """读取并输出本地已保存的历史分析记录"""
    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("\n========== 历史记录列表 ==========")
            print(content if content.strip() else "暂无历史记录。")
            print("==================================\n")
    except FileNotFoundError:
        print("【提示】当前还没有历史记录文件。\n")

# ==================== 4. 交互主循环 ====================

def main():
    while True:
        res = parse_numbers()

        if res == 'q':
            print("程序已安全退出。")
            break
        elif res == 'h':
            read_history()
            continue
        elif res is not None:
            stats = analyzer_numbers(res)
            print_result(res, stats)
            save_result(res, stats)

if __name__ == "__main__":
    main()
