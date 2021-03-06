# Word Break

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(s)
        ans = [False for i in range(N+1)]
        ans[0] = True
        for index in range(N):
            if ans[index]:
                for word in wordDict:
                    L = len(word)
                    if index+L <= N and s[index:index+L] == word:
                        ans[index+L] = True
        return ans[-1]
