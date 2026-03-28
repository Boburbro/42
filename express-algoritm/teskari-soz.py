def reverseString1(s: list) -> list:
    return s[::-1]

def reverseString2(s: list) -> list:
    return s.reverse()

def reverseString3(s: list) -> list:
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
    return s

def reverseString4(s: list) -> list:
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

if __name__ == "__main__":
    from speed_tester import test_speed


    test_speed(lambda: reverseString1(["h", "e", "l", "l", "o"]))
    test_speed(lambda: reverseString2(["h", "e", "l", "l", "o"]))
    test_speed(lambda: reverseString3(["h", "e", "l", "l", "o"]))
    test_speed(lambda: reverseString4(["h", "e", "l", "l", "o"]))
