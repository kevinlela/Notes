### Longest Uncommon Subsequence II
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].

[leetcode](https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/)

### Answer
Pair to pair comparison, O(N^2)

the result is 
1) it is not a subtring of any longer string
2) there is no equivilant string

use a array length 50 as length hashmap, every entry store a set record occurence


class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        map<int, unordered_map<string, int>, std::greater<int>> idx;
        for (int i = 0; i < strs.size(); ++i)
        {
            idx[strs[i].size()][strs[i]]++;
        }
        
        vector<string> badGuys;
        for (auto iter = idx.begin(); iter != idx.end(); ++iter)
        {
            for (auto it = iter->second.begin(); 
                      it != iter->second.end(); ++it)
            {
                if (it->second == 1 && 
                    examine(badGuys, it->first)) return iter->first;
            }
            for (auto it = iter->second.begin(); 
                      it != iter->second.end(); ++it)
            {
                badGuys.push_back(it->first);
            }
        }
        
        return -1;
    }
    
    bool examine(const vector<string> &cand, const string &target)
    {
        for (int i = 0; i < cand.size(); ++i)
        {
            if (isSubStr(cand[i], target)) return false;
        }
        return true;
    }
    
    bool isSubStr(const string &L, const string &S)
    {
        int iter = 0;
        int sLen = S.size();
        for (int i = 0; i < L.size() && iter < sLen; ++i)
        {
            if (L[i] == S[iter]) ++iter;
        }
        
        if (iter == sLen) return true;
        return false;
    }
};