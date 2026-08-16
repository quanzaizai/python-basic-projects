"""
💡【知识点】实时汇率查询工具 (requests 网络请求与 REST API 解析)
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. HTTP GET 请求：使用 requests.get 访问开放汇率 API，设置超时保护 timeout。
  2. JSON 数据解析：response.json() 将接口返回的 JSON 字符串自动转换为 Python 字典。
  3. 防御性异常处理：使用 try-except 捕获网络超时与连接中断。
--------------------------------------------------------------------------------
"""

import requests

API_URL = "https://open.er-api.com/v6/latest/USD"

# ==================== 1. 网络请求与数据获取 ====================

def fetch_rates():
    """从开放汇率接口拉取最新汇率字典"""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("result") == "success":
            return data.get("rates", {})
    except Exception as e:
        print(f"⚠️ 获取汇率失败: {e}")
    return None

# ==================== 2. 主流程与汇率展示 ====================

def main():
    print("=== 实时汇率查询器 (基准货币: 1 USD) ===")
    rates = fetch_rates()
    if not rates:
        print("⚠️ 无法连接汇率接口，请检查网络连接！")
        return

    cny = rates.get("CNY", 0)
    eur = rates.get("EUR", 0)
    jpy = rates.get("JPY", 0)
    gbp = rates.get("GBP", 0)

    print(f"  • 1 美元 (USD) = {cny:.4f} 人民币 (CNY)")
    print(f"  • 1 美元 (USD) = {eur:.4f} 欧元   (EUR)")
    print(f"  • 1 美元 (USD) = {jpy:.4f} 日元   (JPY)")
    print(f"  • 1 美元 (USD) = {gbp:.4f} 英镑   (GBP)")

if __name__ == "__main__":
    main()
