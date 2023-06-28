def isPalindrome(self, s):
    return s[::] == s[::-1]


s = "Listowel"
value = isPalindrome(s)
print(value)
