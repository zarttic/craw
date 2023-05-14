from wordcloud import WordCloud


def gen_from_txt(filename, pic_name):
    # filename = "filename"
    file = open(filename, "r")

    word_frequencies = {}

    for word in file.read().split(","):
        # print(word)
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    print(word_frequencies)
    wordcloud = WordCloud(width=1000, height=700, background_color='white',
                          font_path="lang.ttf").generate_from_frequencies(
        word_frequencies)

    wordcloud.to_file(pic_name)


def gen_from_text(text, pic_name):
    wordcloud = WordCloud(width=1000, height=700, background_color='white',
                          font_path="lang.ttf").generate_from_text(
        text)

    wordcloud.to_file(pic_name)
