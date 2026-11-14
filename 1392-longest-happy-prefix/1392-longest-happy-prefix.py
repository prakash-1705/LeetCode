class Solution(object):
    def lcs(self,s):
        n = len(s)
        lps = [0]*n
        i = 1
        l = 0
        while(i<n):
            if(s[i]==s[l]):
                l += 1
                lps[i] = l
                i += 1
            else:
                if(l>0):
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return l
    def longestPrefix(self, s):
        k = self.lcs(s)
        return s[:k]
        