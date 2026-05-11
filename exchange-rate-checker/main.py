import requests

def get_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"], data["date"]

def convert(rates, from_currency, to_currency, amount):
    
    if from_currency not in rates:
        print(f"不支持的货币:{from_currency}")
        return
    if to_currency not in rates:
        print(f"不支持的货币:{to_currency}")
        return
    
    in_usd = amount / rates[from_currency]
    result = in_usd * rates[to_currency]
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

def main():
    print("正在获取最新汇率...")
    rates, date = get_rates()
    print(f"数据日期：{date}\n")

    print(f"1 USD = {rates['CNY']} CNY（人民币）")
    print(f"1 USD = {rates['EUR']} EUR（欧元）")
    print(f"1 USD = {rates['JPY']} JPY（日元）")
    print()

    while True:
        from_currency = input("输入原始货币（如 CNY），输入 q 退出：").upper()
        if from_currency == "Q":
            print("程序结束")
            break

        to_currency = input("输入目标货币（如 USD）：").upper()
        
        amount_text = input("输入金额：")
        try:
            amount = float(amount_text)
        except ValueError:
            print("请输入正确的数字")
            continue

        convert(rates, from_currency, to_currency, amount)
        print()

if __name__ == "__main__":
    main()