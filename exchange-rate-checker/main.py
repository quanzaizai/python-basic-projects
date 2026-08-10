"""
💡【知识点】RESTful API 网络请求与实时汇率换算引擎
--------------------------------------------------------------------------------
📌【概念与本质】
  1. HTTP GET 请求：通过 requests.get() 访问第三方金融汇率 API 获取实时 JSON 数据。
  2. 基准货币桥接换算 (Base Currency Conversion)：
     - API 以 USD 为基准货币，换算公式：
       Amount_in_USD = Amount / Rate(From)
       Target_Amount = Amount_in_USD * Rate(To)
  3. 防御性异常处理：校验货币代码是否存在，捕获金额输入的 ValueError。

📌【架构与模块分工】
  1. get_rates() : API 数据抓取与 JSON 解析。
  2. convert()   : 汇率多币种交叉换算与格式化打印。
  3. main()      : 交互式 CLI 主循环（支持 q 退出与错误恢复）。
--------------------------------------------------------------------------------
"""

import requests

# ==================== 1. API 汇率获取模块 ====================

def get_rates():
    """从公开 API 获取以美元 (USD) 为基准的实时汇率字典与数据更新日期"""
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("rates", {}), data.get("date", "未知")
    except requests.RequestException as e:
        print(f"【网络错误】获取汇率失败: {e}")
        return None, None

# ==================== 2. 核心货币换算引擎 ====================

def convert(rates, from_currency, to_currency, amount):
    """根据基准汇率字典，计算任意两种法定货币之间的兑换金额"""
    if from_currency not in rates:
        print(f"【错误】不支持的源货币代码: {from_currency}")
        return
    if to_currency not in rates:
        print(f"【错误】不支持的目标货币代码: {to_currency}")
        return
    
    # 经由 USD 作为中间桥梁进行交叉换算
    in_usd = amount / rates[from_currency]
    result = in_usd * rates[to_currency]
    print(f"--> 兑换结果: {amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")

# ==================== 3. 交互式主驱动程序 ====================

def main():
    print("正在从 API 获取最新汇率数据...")
    rates, date = get_rates()
    if not rates:
        return

    print(f"=== 汇率数据基准日期: {date} ===")
    print(f"1 USD = {rates.get('CNY', 0):.4f} CNY (人民币)")
    print(f"1 USD = {rates.get('EUR', 0):.4f} EUR (欧元)")
    print(f"1 USD = {rates.get('JPY', 0):.4f} JPY (日元)")
    print("-" * 40)

    while True:
        from_curr = input("输入原始货币代码 (如 CNY，输入 Q 退出): ").strip().upper()
        if from_curr == "Q":
            print("感谢使用，程序已退出。")
            break

        to_curr = input("输入目标货币代码 (如 USD / EUR): ").strip().upper()
        
        amount_text = input("输入兑换金额: ").strip()
        try:
            amount = float(amount_text)
            if amount < 0:
                print("【错误】金额不能为负数！\n")
                continue
        except ValueError:
            print("【错误】请输入有效的数值金额！\n")
            continue

        convert(rates, from_curr, to_curr, amount)
        print()

if __name__ == "__main__":
    main()