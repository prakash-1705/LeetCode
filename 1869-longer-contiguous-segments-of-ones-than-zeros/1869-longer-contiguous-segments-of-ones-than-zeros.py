class Solution(object):
    def checkZeroOnes(self, s):
        c1 , c2 , m1 , m2 , = 0 , 0 , 0 , 0 
        for i in range(len(s)):
            if(s[i]=='1'):
                c1 += 1
                m1 = max(c1,m1)
                c2 = 0
            else:
                c2 += 1
                m2 = max(c2,m2)
                c1 = 0 

        if(m1>m2):
            return True
        else:
            return False
        