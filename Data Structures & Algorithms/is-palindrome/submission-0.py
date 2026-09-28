class Solution:
    def __isAlphaNumeric(self, char: str) -> bool:
        conditionOne = ord('A') <= ord(char) <= ord('Z')
        conditionTwo = ord('a') <= ord(char) <= ord('z')
        conditionThree = ord('0') <= ord(char) <= ord('9')
        return (conditionOne or conditionTwo or conditionThree)
    
    def isPalindrome(self, s: str) -> bool:
        if (s is None or len(s) <= 1):
            return True
        
        l, r = 0, len(s) - 1
        while (l < r):
            while (l < r and not self.__isAlphaNumeric(s[l])):
                l += 1
            while (l < r and not self.__isAlphaNumeric(s[r])):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        