"""
=============================================================================
💡【知识点】Python 基础实战 —— 数字特征分析器 (Number Property Analyzer)
=============================================================================

📌【1. 核心功能与数学原理】
  - 奇偶性判定 (Parity)   : 利用模运算 `num % 2 == 0`，若余数为 0 则为偶数，否则为奇数。
  - 素数检测 (Prime Check) : 
    - 素数定义：大于 1 且只能被 1 和自身整除的自然数。
    - 🔍 复杂度优化核心：如果 $n = a \times b$，则必有 $\min(a, b) \le \sqrt{n}$。
      因此只需遍历 $[2, \lfloor\sqrt{n}\rfloor]$，时间复杂度从 $O(N)$ 暴降至 $O(\sqrt{N})$！
  - 因数分解 (Factors)    : 查找所有能整除 $n$ 的正整数集合。
  - 文件持久化 (File I/O)  : 使用上下文管理器 `with open(..., 'a')` 以追加模式安全持久化历史。

📌【2. 程序执行流程与架构图解】

  [用户输入] (如: 28)
       |
       v
  [异常捕获] (try-except 防止非数字或负数崩溃)
       |
       +---> ① 奇偶判定 (num % 2) --------> "偶数"
       +---> ② 素数筛选 (O(sqrt(N))) -----> "不是素数"
       +---> ③ 因数枚举 ([1..N]) ---------> [1, 2, 4, 7, 14, 28]
       |
       +---> 格式化控制台彩色输出
       +---> `with open('history.txt', 'a')` 自动关闭文件流追加日志

📌【3. 深度思考与高频 Q&A】

  ❓ Q1: 为什么素数检查只需要循环到 `math.isqrt(n) + 1`？
     👉 解答：因数总是成对出现的（例如 36 = 2×18 = 3×12 = 4×9 = 6×6）。
        如果一个数在 $\sqrt{n}$ 之前没有任何因数，那么在 $\sqrt{n}$ 之后也绝对不可能存在因数。

  ❓ Q2: 为什么写入文件必须用 `with open` 而不是 `f = open(); ...; f.close()`？
     👉 解答：`with` 是 Python 的上下文管理器协议。即使写入过程中发生异常崩溃，
        Python 解释器也能 100% 确保文件描述符被安全关闭，杜绝句柄泄漏。
=============================================================================
"""

# ==================== 0. 标准库模块引入与作用解析 ====================
import math               # 数学函数库：提供 isqrt() 进行平方根快速开方与因数上限计算
from datetime import datetime  # 日期时间库：提供 now() 与 strftime() 生成操作审计时间戳


# ==================== 1. 核心数学分析函数 ====================

def is_prime(n: int) -> bool:
    """
    判断一个给定的正整数是否为素数 (质数)

    :param n: 待检测的正整数
    :return: True 为素数, False 为合数或非素数(<2)
    :note: 时间复杂度 O(sqrt(N)) | 空间复杂度 O(1)
    """
    # 【步骤 1】边界过滤：小于 2 的整数（如 0, 1, 负数）都不是素数
    if n < 2:
        return False
    
    # 2 是唯一的偶素数
    if n == 2:
        return True
    
    # 排除所有大于 2 的偶数（常数级剪枝优化）
    if n % 2 == 0:
        return False

    # 【步骤 2】从 3 开始遍历到 sqrt(n)，步长为 2 (只检查奇数因数)
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False  # 找到可整除因数，直接判定为非素数

    return True  # 未找到任何因数，确认为素数


def get_factors(n: int) -> list[int]:
    """
    计算并返回一个正整数的所有正因数列表

    :param n: 目标正整数
    :return: 升序排列的正因数列表
    :note: 时间复杂度 O(N) | 空间复杂度 O(K) (K 为因数个数)
    """
    factors = []
    # 从 1 遍历到 n，收集所有整除数
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# ==================== 2. 主流程与交互入口 ====================

def main() -> None:
    """程序交互主入口"""
    print("=" * 45)
    print("        🔢 数字特征全维度智能分析器        ")
    print("=" * 45)

    # 【步骤 1】健壮的用户输入解析与异常防御
    try:
        user_input = input("👉 请输入一个正整数: ").strip()
        num = int(user_input)
        if num <= 0:
            print("⚠️ [输入非法] 请输入严格大于 0 的正整数！")
            return
    except ValueError:
        print("⚠️ [输入非法] 无法解析！请输入纯阿拉伯数字。")
        return

    # 【步骤 2】执行各项数学特征分析
    parity = "偶数 (Even)" if num % 2 == 0 else "奇数 (Odd)"
    prime_status = "✅ 是素数 (Prime)" if is_prime(num) else "❌ 不是素数 (Composite)"
    factors = get_factors(num)

    # 构造带时间戳的审计日志记录
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] 数字: {num} | 奇偶: {parity} | "
        f"素数属性: {prime_status} | 因数个数: {len(factors)} 个 -> {factors}"
    )

    # 【步骤 3】控制台美化格式输出
    print("\n" + "-" * 20 + " 📊 分析结果 " + "-" * 20)
    print(f"  • 输入数值: {num}")
    print(f"  • 奇偶性质: {parity}")
    print(f"  • 素数检测: {prime_status}")
    print(f"  • 因数列表: {factors} (共 {len(factors)} 个)")
    print("-" * 52)

    # 【步骤 4】持久化追加写入历史文件 (history.txt)
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
        print("💾 分析记录已安全追加至 [history.txt]")
    except IOError as e:
        print(f"⚠️ [写入失败] 无法写入历史记录: {e}")


if __name__ == "__main__":
    main()
