class Solution:
    def __getFrequencyString(self, word: str) -> str:
        freqs = [0] * 26
        
        for char in word:
            index = ord(char) - ord('a')
            freqs[index] += 1
        
        return ",".join([str(count) for count in freqs])
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (strs is None):
            return None
        result = []
        anagramsDict = defaultdict(list)

        for word in strs:
            key = self.__getFrequencyString(word)
            anagramsDict[key].append(word)
        
        for k, v in anagramsDict.items():
            result.append(v)
        
        return result