import re

from wordcloud import WordCloud

def rex(s):
    pattern = r'(?<=>)[a-zA-Z0-9]+(?=<)'
    match = re.search(pattern, s)
    if match:
        return match.group()
    else:
        return " "
