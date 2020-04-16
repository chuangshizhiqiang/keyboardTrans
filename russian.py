#coding=utf-8

import sys

directory = {
    "a":"ф",
    "b":"и",
    "c":"с",
    "d":"в",
    "e":"у",
    "f":"а",
    "g":"п",
    "h":"р",
    "i":"ш",
    "j":"о",
    "k":"л",
    "l":"д",
    "m":"ь",
    "n":"т",
    "o":"щ",
    "p":"з",
    "q":"й",
    "r":"к",
    "s":"ы",
    "t":"е",
    "u":"г",
    "v":"м",
    "w":"ц",
    "x":"ч",
    "y":"н",
    "z":"я",
}

# 英文键盘输入俄语翻译器

def trans(data):
    res = ""
    for x in data:
        res += directory[x]
    return res

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Need input string")
        sys.exit()

    res = trans(sys.argv[1])
    print(res)
    pass