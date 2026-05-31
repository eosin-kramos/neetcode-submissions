class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            if i.isalnum():
                string += i
        
        i = 0
        j = len(string) - 1

        while i <= j:
            if string[i].lower() != string[j].lower():
                return False
            i += 1
            j -= 1
        
        return True