class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += s
            string += "."
        
        return string

    def decode(self, s: str) -> List[str]:
        strings = []

        string = ""
        for c in s:
            if c == ".":
                strings.append(string)
                string = ""
            else:
                string = string + c
        
        return strings
        
