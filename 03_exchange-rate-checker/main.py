"""
=============================================================================
💡【知识点】Python 基础实战 —— 实时汇率查询工具 (Exchange Rate Checker)
=============================================================================

📌【1. 核心技术栈与网络请求原理】
  - HTTP 客户端 (requests) : Python 最主流的第三方 HTTP 库，用于向远程 API 发起网络请求。
  - RESTful API 交互流程 :
    
    [Python 客户端] -------- HTTP GET (API_URL) --------> [开放汇率服务器]
           |                                                      |
           | <--- 200 OK + JSON {"result":"success", "rates":{}} -+
           v
    [response.json()] 自动反序列化为 Python 字典并提取币种汇率

  - 生产级防御机制 :
    - `timeout=10` : 避免因网络波动或接口卡死导致程序无休止挂起。
    - `response.raise_for_status()` : 遇到 404, 500 等 HTTP 错误状态码时主动抛出异常。
    - `try-except` : 捕获网络断开、DNS 解析失败等所有潜在通信错误。
=============================================================================
"""

import requests
from typing import Optional, Dict

# 免费公开的实时外汇汇率 REST API 端点 (以美元 USD 为基础货币)
API_URL = "https://open.er-api.com/v6/latest/USD"


# ==================== 1. 网络请求与数据获取 ====================

def fetch_rates() -> Optional[Dict[str, float]]:
    """
    向远程 API 发起 HTTP 请求并解析返回的全球汇率字典

    :return: 包含各币种汇率的字典 (如 {"CNY": 7.23, "EUR": 0.92})；失败时返回 None
    """
    try:
        # 【步骤 1】发起 GET 请求，设置 10 秒超时防护
        response = requests.get(API_URL, timeout=10)
        
        # 【步骤 2】检查 HTTP 状态码是否为 200 OK
        response.raise_for_status()

        # 【步骤 3】将 JSON 响应体自动反序列化为 Python 字典
        data = response.json()

        # 【步骤 4】业务逻辑校验：确认接口返回标志为成功
        if data.get("result") == "success":
            return data.get("rates", {})
        else:
            print("⚠️ 接口返回业务异常，未获取到有效数据。")
            return None

    except requests.exceptions.Timeout:
        print("⚠️ [网络异常] 请求接口超时，请检查您的网络连接！")
    except requests.exceptions.ConnectionError:
        print("⚠️ [网络异常] 无法连接到远程汇率服务器。")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ [HTTP 错误] 服务端返回错误状态码: {e}")
    except Exception as e:
        print(f"⚠️ [未知异常] 数据解析失败: {e}")

    return None


# ==================== 2. 主流程与汇率展示 ====================

def main() -> None:
    """汇率查询器主程序"""
    print("=" * 45)
    print("       💱 全球实时汇率查询器 (Base: 1 USD)       ")
    print("=" * 45)
    print("⏳ 正在从云端拉取最新外汇市场数据，请稍候...\n")

    rates = fetch_rates()

    if not rates:
        print("❌ 汇率拉取失败，程序已安全终止。")
        return

    # 提取主流全球货币汇率并进行安全取值 (若币种不存在则缺省为 0.0)
    cny = rates.get("CNY", 0.0)
    eur = rates.get("EUR", 0.0)
    jpy = rates.get("JPY", 0.0)
    gbp = rates.get("GBP", 0.0)
    hkd = rates.get("HKD", 0.0)

    # 格式化打印当前牌价
    print("✅ 数据同步成功！当前最新基准汇率如下：")
    print("-" * 45)
    print(f"  • 🇨🇳 1 美元 (USD) = {cny:8.4f} 人民币 (CNY)")
    print(f"  • 🇪🇺 1 美元 (USD) = {eur:8.4f} 欧元   (EUR)")
    print(f"  • 🇯🇵 1 美元 (USD) = {jpy:8.4f} 日元   (JPY)")
    print(f"  • 🇬🇧 1 美元 (USD) = {gbp:8.4f} 英镑   (GBP)")
    print(f"  • 🇭🇰 1 美元 (USD) = {hkd:8.4f} 港币   (HKD)")
    print("-" * 45)


if __name__ == "__main__":
    main()
