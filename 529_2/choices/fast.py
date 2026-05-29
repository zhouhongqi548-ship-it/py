from random import choice  # 從random模組匯入choice函式

places = ["McDonals", "KFC", "Berger King", "Moses", "Wendys"]

def pick():
    return choice(places)

print(pick())
