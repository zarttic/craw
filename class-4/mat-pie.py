import matplotlib.pyplot as plt

file = open("../words.txt", "r")

word_frequencies = {}
all = 0
for word in file.read().split(","):
    word_frequencies[word] = word_frequencies.get(word, 0) + 1
    all += 1

labels = ["ELSE"]  # 标签
sizes = [0]  # 每一块的大小
# 份额过小不计算
for i in word_frequencies:
    cur = word_frequencies[i] * 100 / all
    if cur < 2:
        sizes[0] += cur
    else:
        labels.append(i)
        sizes.append(cur)

print(labels)
print(sizes)
# 饼状图参数
explode = (0.2, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.2, 0.3)  # 用于突出某一部分

# 绘图
plt.pie(sizes, labels=labels, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
