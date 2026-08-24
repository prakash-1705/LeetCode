class Solution(object):
    def distributeCandies(self, candies, num_people):
        arr = [0] * num_people
        temp = candies
        give = 1
        i = 0

        while temp > 0:
            current = min(give, temp)
            arr[i % num_people] += current

            temp -= current
            give += 1
            i += 1

        return arr
        