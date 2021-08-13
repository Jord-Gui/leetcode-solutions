# Group Anagrams
# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3887/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            base = ''.join(sorted(word))
            if base in anagram:
                anagram[base].append(word)
            else:
                anagram[base] = [word]
        ret_val = []
        for key in anagram:
            ret_val.append(anagram[key])
        return ret_val
