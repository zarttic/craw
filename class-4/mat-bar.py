import matplotlib.pyplot as plt



file = open("../words.txt", "r")

word_frequencies = {}
all = 0
for word in file.read().split(","):
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

# 数据
langs = []
cnts = []
for i in word_frequencies:
    if word_frequencies[i] < 10:
        continue
    langs.append(i)
    cnts.append(word_frequencies[i])
# 绘图
plt.figure(figsize=(10,10))
plt.bar(langs, cnts)

# 添加图表标题和轴标签

plt.title('langs')
plt.xlabel('lang')
plt.ylabel('data')
# plt.tight_layout()
plt.show()