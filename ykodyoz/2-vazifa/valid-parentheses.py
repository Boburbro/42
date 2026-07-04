class Solution:
    def isValid(self, s: str) -> bool:
        _stack = []
        for ch in s:
            if ch in "({[": _stack.append(ch)
            if ch in ")}]":
                if _stack == []:
                    return False
                _value = _stack.pop()
                if _value == "(" and ch != ")":
                    return False
                
                if _value == "[" and ch != "]":
                    return False

                if _value == "{" and ch != "}":
                    return False
                
        
        return _stack == []

print(Solution().isValid("([)]"))  # False "([)]"