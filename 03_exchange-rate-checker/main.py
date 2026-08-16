"""
【知识点】实时汇率查询工具 (requests 与开放 API)
--------------------------------------------------------------------------------
1. 网络请求：使用 requests.get 调用汇率 API。
2. JSON 解析：解析响应数据并提取汇率字典。
3. 异常处理：try-except 捕获网络超时与连接异常。
--------------------------------------------------------------------------------
"""

import requests

API_URL = "https://open.er-api.com/v6/latest/USD"

def fetch_rates():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("result") == "success":
            return data.get("rates", {})
    except Exception as e:
        print(f"获取汇率失败: {e}")
    return None

def main():
    print("=== 实时汇率查询器 (基准: 1 USD) ===")
    rates = fetch_rates()
    if not rates:
        print("无法连接汇率接口，请检查网络！")
        return

    cny = rates.get("CNY", 0)
    eur = rates.get("EUR", 0)
    jpy = rates.get("JPY", 0)
    gbp = rates.get("GBP", 0)

    print(f"1 美元 (USD) = {cny:.4f} 人民币 (CNY)")
    print(f"1 美元 (USD) = {eur:.4f} 欧元   (EUR)")
    print(f"1 美元 (USD) = {jpy:.4f} 日元   (JPY)")
    print(f"1 美元 (USD) = {gbp:.4f} 英镑   (GBP)")

if __name__ == "__main__":
    main()
