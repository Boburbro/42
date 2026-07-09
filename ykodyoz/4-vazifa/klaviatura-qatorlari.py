set1 = set("qwertyuiop")
set2 = set("asdfghjkl")
set3 = set("zxcvbnm")

def findWords(words: list) -> set:
    return sorted(set(
        word for word in words if set(word.lower()).issubset(set1) or set(word.lower()).issubset(set2) or set(word.lower()).issubset(set3)
    ))


print(findWords(["Hello","Alaska","Dad","Peace"]))