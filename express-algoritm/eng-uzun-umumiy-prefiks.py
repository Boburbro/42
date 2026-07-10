def longestCommonPrefix(words: list) -> str:
    prefix = words[0]

    for word in words:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix
