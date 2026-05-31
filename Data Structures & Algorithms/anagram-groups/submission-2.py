#Iterate through each string in strs
#get the ord() and create an array for each string
#put those ord() array values into a hash Map
#Iterate through that hashmap and add to a list
 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordMap = dict()
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in ordMap:
                ordMap[tuple(count)].append(string)
            else:
                ordMap[tuple(count)] = [string]
        
        output = []
        for key, value in ordMap.items():
            group = []
            for val in value:
                group.append(val)
            output.append(group)

        return output


        
            
            
        
        