class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            for char in word:
                encoded += str(ord(char)) + ';'
            encoded += '#'
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        strings = s.split("#")
        for string in strings[:-1]:
            if string == '':
                res.append('') 
            else:
                chars = string.split(';')
                decoded_str = ''
                for num in chars:
                    if num: 
                        decoded_str += chr(int(num))
                res.append(decoded_str)

        return res