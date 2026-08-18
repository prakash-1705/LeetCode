class Solution(object):
    def largestInteger(self, nums, k):
        left , right = 0 , k-1
        countlist = [0] * (max(nums) + 1)
        while(right!=len(nums)):
            seen = set()
            for i in range(left, right + 1):
                if nums[i] not in seen:
                    countlist[nums[i]] += 1
                    seen.add(nums[i])
            right += 1
            left += 1
        ans = -1
        for i in range(len(countlist)):
            if countlist[i] == 1:
                ans = i
        return ans
        

        