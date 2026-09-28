class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        frequencies = {}
        for char in s:
            if (char not in frequencies):
                frequencies[char] = 0
            frequencies[char] += 1
        
        for char in t:
            if (char not in frequencies):
                return False
            frequencies[char] -= 1

        for char in frequencies:
            if frequencies[char] != 0:
                return False
        
        return True