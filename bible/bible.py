#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""
import re
import string
from collections import Counter
from pathlib import Path

f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    words = re.split('[' + string.punctuation + ' \n]', BIBLE)
    words = [w.lower() for w in words if w and not w.isdigit()]

    ordered = Counter(words).most_common(n)

    return [k[0] for k in ordered]


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
