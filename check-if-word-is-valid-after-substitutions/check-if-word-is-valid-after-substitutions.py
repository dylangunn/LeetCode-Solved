class Solution:
    def isValid(self, s: str) -> bool:
        if s.count('a') == s.count('b') == s.count('c'):
            at = s.find("abc")
            while at != -1:
                s = s[:at] + s[at+3:]
                at = s.find("abc")
            if s == "":
                return True
            return False
        else:
            return False