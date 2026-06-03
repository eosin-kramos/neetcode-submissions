# Go through each string and create an array that holds letterss.
# Array will be length of the aplhabet.
# looking at each string, we count how many of each letter in that word and add that in array.
# ex: 'car' = [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
# we do this by iterating through strs, then iterate through that string in strs
# then put that array in a Map. Would have to use tuple (key) as it is immutable, and place word as value
# iterate through the map and put it and append to output
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            group = self.charCount(word)
            group = tuple(group)
            if group in groups:
                groups[group].append(word)
            else:
                groups[group] = [word]
        
        result = []

        for value in groups.values():
            result.append(value)

        return result
    
    def charCount(self, word: str) -> List[int]:
        result = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            result[index] += 1
        return result
    

        