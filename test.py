from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


# 读取数据
df = pd.read_csv('data.csv')

# 将数据拼接成一个字符串
text = ' '.join(df['content'].values)

# 将所有单词转换为小写，并计算它们的出现频率
word_frequencies = {}
for word in text.lower().split():
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

# 生成词云
wordcloud = WordCloud(width=800, height=400, max_words=500, background_color='white').generate_from_frequencies(word_frequencies)

# 绘制词云图
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()