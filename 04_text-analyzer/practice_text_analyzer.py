"""
💡【知识点】基础文本分析：英文字词统计与指标度量
--------------------------------------------------------------------------------
📌【核心思想与本质】
  1. splitlines()：按换行符拆分文本行。
  2. split()：默认按任意空白字符拆分单词序列。
--------------------------------------------------------------------------------
"""

def analyze_english_text(text: str):
    lines = text.strip().splitlines()
    words = text.split()
    chars = len(text)

    print("=== 英文文本核心指标 ===")
    print(f"  • 总行数:   {len(lines)} 行")
    print(f"  • 总词数:   {len(words)} 个单词")
    print(f"  • 总字符数: {chars} 个字符")

if __name__ == "__main__":
    sample = """Hello World
Python is fun and easy to learn.
Let us build great software!"""
    analyze_english_text(sample)
