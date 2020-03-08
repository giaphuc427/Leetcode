# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def defineRomanCharacter(self, s):
        char = {
            'I':1,
            'V':5,
            'IV':4,
            'X':10,
            'IX':9,
            'L':50,
            'XL':40,
            'C':100,
            'XC':90,
            'D':500,
            'CD':400,
            'M':1000,
            'CM':900
        }
        return char.get(s,-1000)

    def romanToInt(self, s):
        sum = 0
        if len(s) > 1:
            pointer1 = 1
        else:
            pointer1 = 0
        pointer2 = 0
        while pointer2 < len(s):
            if pointer1 >= len(s):
                pointer1 = pointer2
            if self.defineRomanCharacter(s[pointer2] + s[pointer1]) > 0:
                sum = sum + self.defineRomanCharacter(s[pointer2] + s[pointer1])
                pointer2 = pointer1 + 1
                pointer1 = pointer2 + 1               
            else:
                sum = sum + self.defineRomanCharacter(s[pointer2])
                pointer1 = pointer1 + 1
                pointer2 = pointer2 + 1
        return sum

a = Solution()
print(a.romanToInt('LVIII'))
        