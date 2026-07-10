from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    cRansonNote = Counter(ransomNote)
    cMagazine = Counter(magazine)

    for key, value in cRansonNote.items():
        if cMagazine[key] < value:
            return False

    return True


print(canConstruct("aa ", "aaa"))
