class Solution(object):
    def distributeCandies(self, candies, num_people):
        ans=[0]*num_people
        count=1
        while candies>0:
            for i in range(num_people):
                if candies<=count:
                    ans[i]+=candies
                    candies-=candies
                    break
                else:
                    candies-=count
                    ans[i]+=count
                    count+=1
        return ans
        