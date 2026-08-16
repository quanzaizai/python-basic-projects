"""
💡【知识点】数字特征分析器 (奇偶性、素数检测、因数分解与历史记录)
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. 奇偶判定：整数取模 (num % 2 == 0) 为偶数，否则为奇数。
  2. 素数检测：从 2 遍历至 sqrt(n)，若期间存在可整除因子则非素数，时间复杂度 O(sqrt(N))。
  3. 文件持久化：使用 Python 上下文管理器 (with open) 以追加模式 ('a') 安全写入历史。
--------------------------------------------------------------------------------
"""

import math
from datetime import datetime

# ==================== 1. 核心数学分析函数 ====================

def is_prime(n: int) -> bool:
    """判断一个整数是否为素数"""
    if n < 2:
        return False
    # 🔍【性能优化】：因数成对出现，只需检查到 sqrt(n) 即可
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

# ==================== 2. 主流程与交互入口 ====================

def main():
    print("=== 数字特征分析器 ===")
    try:
        num = int(input("请输入一个正整数: ").strip())
        if num <= 0:
            print("⚠️ 请输入大于 0 的正整数！")
            return
    except ValueError:
        print("⚠️ 输入无效：请输入纯数字！")
        return

    # 1. 执行特征分析
    parity = "偶数" if num % 2 == 0 else "奇数"
    prime_status = "是素数" if is_prime(num) else "不是素数"
    factors = get_factors(num)

    result_text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 数字: {num}, 奇偶: {parity}, 素数: {prime_status}, 因数: {factors}"

    # 2. 控制台格式化输出
    print("\n--- 分析结果 ---")
    print(f"  • 输入数字: {num}")
    print(f"  • 奇偶性质: {parity}")
    print(f"  • 素数属性: {prime_status}")
    print(f"  • 所有因数: {factors}")

    # 3. 追加写入历史记录文件
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(result_text + "\n")
    print("✅ 结果已成功保存至 history.txt")

if __name__ == "__main__":
    main()
