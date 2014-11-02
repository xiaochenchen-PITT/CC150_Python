class Solution:
    # @return an integer
    def romanToInt(self, s):
        n = 0
        prev = ''
        for c in s:
            if c == 'I':
                n += 1
            elif c == 'V':
                if prev =='I':
                    n += 3
                else:
                    n += 5
            elif c == 'X':
                if prev == 'I':
                    n += 8
                else:
                    n += 10
            elif c == 'L':
                if prev == 'X':
                    n += 30
                else:
                    n += 50
            elif c == 'C':
                if prev == 'X':
                    n += 80
                else:
                    n += 100
            elif c == 'D':
                if prev == 'C':
                    n += 300
                else:
                    n += 500
            else:
                if prev == 'C':
                    n += 800
                else:
                    n += 1000
            prev = c
        return n 