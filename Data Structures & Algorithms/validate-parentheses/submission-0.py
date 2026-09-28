class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char not in bracketsMap:
                stack.append(char)
            else:
                openingBracket = bracketsMap[char]
                if not stack or stack[-1] != openingBracket:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0 
        