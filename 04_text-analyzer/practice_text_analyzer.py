"""
【知识点】文本分析练习：英文字词统计与行数统计
--------------------------------------------------------------------------------
1. 字符串清洗与拆分：lower() 转小写，split() 拆分单词。
2. 文本基础指标：统计行数、字符数与词数。
--------------------------------------------------------------------------------
"""

def analyze_english_text(text: str):
    lines = text.strip().splitlines()
    words = text.split()
    chars = len(text)

    print("=== 英文文本指标 ===")
    print(f"总行数:   {len(lines)}")
    print(f"总词数:   {len(words)}")
    print(f"总字符数: {chars}")

if __name__ == "__main__":
    sample = """Hello World
Python is fun and easy to learn.
Let us build great software!"""
    analyze_english_text(sample)
