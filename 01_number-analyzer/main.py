"""
【知识点】数字特征分析器 (奇偶性、素数检测与历史记录)
--------------------------------------------------------------------------------
1. 奇偶判定：num % 2 == 0 为偶数。
2. 素数检测：从 2 遍历至 sqrt(num)，若无整除数则为素数。
3. 文件记录：以追加模式 ('a') 将分析结果保存至 history.txt。
--------------------------------------------------------------------------------
"""

import math
from datetime import datetime

def is_prime(n: int) -> bool:
    """判断一个整数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_factors(n: int) -> list[int]:
    """获取数字的所有正因数"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def main():
    print("=== 数字特征分析器 ===")
    try:
        num = int(input("请输入一个正整数: ").strip())
        if num <= 0:
            print("请输入大于 0 的正整数！")
            return
    except ValueError:
        print("输入无效：请输入纯数字！")
        return

    # 1. 特征分析
    parity = "偶数" if num % 2 == 0 else "奇数"
    prime_status = "是素数" if is_prime(num) else "不是素数"
    factors = get_factors(num)

    result_text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 数字: {num}, 奇偶: {parity}, 素数: {prime_status}, 因数: {factors}"

    # 2. 控制台输出
    print("\n--- 分析结果 ---")
    print(f"数字:     {num}")
    print(f"奇偶性:   {parity}")
    print(f"素数属性: {prime_status}")
    print(f"所有因数: {factors}")

    # 3. 追加写入历史记录
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(result_text + "\n")
    print("结果已保存至 history.txt")

if __name__ == "__main__":
    main()
