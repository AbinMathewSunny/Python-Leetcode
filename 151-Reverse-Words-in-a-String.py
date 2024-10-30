class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""
        for word in words[::-1]:
            res += word+" "
        res= res.strip()
        return res    