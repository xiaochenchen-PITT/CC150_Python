class Solution:
    # @return an integer
    def reverse(self, x):
        digit_list = []
        for digit in str(abs(x)):
            digit_list.append(digit)
        if x < 0:
            digit_list.append('-')
        new_string = ''
        reverse_list = digit_list[::-1]
        for digit in reverse_list:
            new_string += str(digit)
        # new_number = int(new_string)
        return int(new_string)
        
        