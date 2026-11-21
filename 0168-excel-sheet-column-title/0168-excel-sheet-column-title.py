class Solution(object):
    def convertToTitle(self, columnNumber):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter = []
        while(columnNumber>0):
            columnNumber -= 1
            remainder = columnNumber % 26
            letter.append(alpha[remainder])
            columnNumber //= 26
        return "".join(reversed(letter))
        