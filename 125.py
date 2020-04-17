# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
            return True
        alphanum_only = ""
        for char in s:
            if char.isalnum():
                alphanum_only += char
        alphanum_only = alphanum_only.lower()
        if alphanum_only == alphanum_only[::-1]:
            return True
        return False
