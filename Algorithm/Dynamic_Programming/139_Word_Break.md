### Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

[leetcode](https://leetcode.com/problems/word-break/description/)

### Answer 
dp[i] represent whether s[0...i] can be represented or not. subtract Or(s[k]) if s[k+1...i] is in the dictionary or not.  

	class Solution {
	public:
	    bool wordBreak(string s, vector<string>& wordDict) {
	        unordered_set<string> wd;
	        set<int> lens;
	        int sLen = s.size();
	        
	        for (auto iter = wordDict.begin(); iter != wordDict.end(); ++iter)
	        {
	            if (iter->size() > sLen) continue;
	            lens.insert(iter->size());
	            wd.insert(*iter);
	        }
	        
	        
	        if (sLen == 0) return false;
	        
	        vector<bool> dp(sLen - 1, false);
	        dp[0] = true;
	        
	        for (int k = 1; k <= sLen; ++k)
	        {
	            for (auto iter = lens.begin(); (*iter) <= k && iter != lens.end(); ++iter)
	            {
	                if (wd.find(s.substr(k - *iter, *iter)) != wd.end())
	                {
	                    dp[k] = dp[k - *iter];
	                }
	                if (dp[k]) break;
	            }
	        }
	        
	        return dp[sLen];
	    }
	};