class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:

            string += str(len(s)) + "." + s
        
        return string

    def decode(self, s: str) -> List[str]:
        strings = []

        num = ""
        string = ""
        count = 0
        for c in s:
            if c == ".":
                count = int(num)
                if not count:
                    strings.append(string)
                    string = ""
                num = ""
                continue
            if count:
                string += c
                count -= 1
                if not count:
                    strings.append(string)
                    string = ""
            else:
                num += c


        
        return strings
        
