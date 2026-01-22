code_map = {
    "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E",
    ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J",
    "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O",
    ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T",
    ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
    "__..": "Z"
}

encrypted = input().strip()
results = []

def decode(index, current):
    if index == len(encrypted):
        results.append(current)
        return

    for code in code_map:
        if encrypted.startswith(code, index):
            decode(index + len(code), current + code_map[code])

decode(0, "")
results.sort()

for word in results:
    print(word)
