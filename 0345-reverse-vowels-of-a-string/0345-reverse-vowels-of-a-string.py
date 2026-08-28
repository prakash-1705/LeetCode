class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        stack = []
        for char in s:
            if char in vowels:
                stack.append(char)
        characters = list(s)
        for i in range(len(characters)):
            if characters[i] in vowels:
                characters[i] = stack.pop()
        return "".join(characters)

        