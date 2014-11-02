class Solution:
    # @return a string
    def intToRoman(self, n):
        s = ''
        while n > 0:
            if n >= 1000:
                n -= 1000
                s += 'M'
            elif n >= 900:
                n -= 900
                s += 'CM'
            elif n >= 500:
                n -= 500
                s += 'D'
            elif n >= 400:
                n -= 400
                s += 'CD'
            elif n >= 100:
                n -= 100
                s += 'C'
            elif n >= 90:
                n -= 90
                s += 'XC'
            elif n >= 50:
                n -= 50
                s += 'L'
            elif n >= 40:
                n -= 40
                s += 'XL'
            elif n >= 10:
                n -= 10
                s += 'X'
            elif n >= 9:
                n -= 9
                s += 'IX'
            elif n >= 5:
                n -= 5
                s += 'V'
            elif n >= 4:
                n -= 4
                s += 'IV'
            else:
                n -= 1
                s += 'I'
        return s
s = Solution()
print s.intToRoman(0)
print s.intToRoman(1)
print s.intToRoman(1991)
print s.intToRoman(1994)
print s.intToRoman(1995)
print s.intToRoman(1996)
print s.intToRoman(2014)
