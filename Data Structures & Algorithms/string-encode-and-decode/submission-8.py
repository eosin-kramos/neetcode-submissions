class Solution:
    #'10#helloworld5#world'
    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = str(len(s))
            output = output + length + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        r = 1
        while l < len(s):
            while s[r] != '#' and r < len(s):
                r += 1
            string_len = int(s[l:r])
            l = r + 1
            r = r + string_len
            output.append(s[l:r + 1])
            l = r + 1
            r = l + 1
        return output




            