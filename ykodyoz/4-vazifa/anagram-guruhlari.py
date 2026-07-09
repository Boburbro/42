def groupAnagrams(words: list) -> int:
    result = dict()

    for word in words:
        sortedWord = "".join(sorted(word))
        result[sortedWord] = result.get(sortedWord, [])
        result[sortedWord].append(word)
    
    return list(result.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))