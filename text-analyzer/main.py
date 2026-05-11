import jieba
import matplotlib.pyplot as plt

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()
words = list(jieba.cut(text))
filtered_words = [word for word in words if len(word) > 1]

from collections import Counter
word_counts = Counter(filtered_words)
top5 = word_counts.most_common(5)
print(top5)

words_list = [item[0] for item in top5]
counts_list = [item[1] for item in top5]

plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.bar(words_list, counts_list)
plt.title("词频统计Top5")
plt.xlabel("词语")
plt.ylabel("出现次数")
plt.show()