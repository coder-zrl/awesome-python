import pypinyin

# 关于style
'''
    普通风格，不带声调。如： 中国 -> ``zhong guo``
    NORMAL = 0

    标准声调风格，拼音声调在韵母第一个字母上（默认风格）。如： 中国 -> ``zhōng guó``
    TONE = 1

    声调风格2，即拼音声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 -> ``zho1ng guo2``
    TONE2 = 2

    声调风格3，即拼音声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``zhong1 guo2``
    TONE3 = 8

    声母风格，只返回各个拼音的声母部分（注：有的拼音没有声母，详见 `#27`_）。如： 中国 -> ``zh g``
    INITIALS = 3

    首字母风格，只返回拼音的首字母部分。如： 中国 -> ``z g``
    FIRST_LETTER = 4

    韵母风格，只返回各个拼音的韵母部分，不带声调。如： 中国 -> ``ong uo``
    FINALS = 5

    标准韵母风格，带声调，声调在韵母第一个字母上。如：中国 -> ``ōng uó``
    FINALS_TONE = 6

    韵母风格2，带声调，声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 -> ``o1ng uo2``
    FINALS_TONE2 = 7

    韵母风格3，带声调，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``ong1 uo2``
    FINALS_TONE3 = 9

    注音风格，带声调，阴平（第一声）不标。如： 中国 -> ``ㄓㄨㄥ ㄍㄨㄛˊ``
    BOPOMOFO = 10

    注音风格，仅首字母。如： 中国 -> ``ㄓ ㄍ``
    BOPOMOFO_FIRST = 11

    汉语拼音与俄语字母对照风格，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 -> ``чжун1 го2``
    CYRILLIC = 12

    汉语拼音与俄语字母对照风格，仅首字母。如： 中国 -> ``ч г``
    CYRILLIC_FIRST = 13
'''

# 不带声调的(style=pypinyin.NORMAL)
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL,heteronym =True):  # heteronym是检测多音字
        s += ''.join(i)
        print(i)
    return s

# 带声调的(默认)
def yinjie(word):
    s = ''
    # heteronym=True开启多音字
    for i in pypinyin.pinyin(word, heteronym=True):
        s = s + ''.join(i) + " "
    return s


if __name__ == "__main__":
    print(pinyin("忠厚传家久"))
    print(yinjie("诗书继世长"))