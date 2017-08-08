### Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

[leetcode](https://leetcode.com/problems/distinct-subsequences/description/)

### Answer

	class Solution {
	public:
	    int numDistinct(string s, string t) {
	        // let dp[i][j] represents the number of substrings in s[0...i] of t[0...j]
	        // dp[i][j] = dp[i-1][j] + dp[i-1][j]; if (s[i] == t[j])
	        //          = dp[i-1][j] if (s[i] != t[j])
	        
	        int sLen = s.size(), tLen = t.size();
	        vector<vector<int>> dp(tLen + 1, vector<int> (sLen + 1, 0));
	        
	        for (int i = 0; i <= sLen; ++i)
	            dp[0][i] = 1;
	        
	        for (int j = 1; j <= tLen; ++j)
	        {
	            for (int i = 1; i <= sLen; ++i)
	            {
	                if (s[i-1] == t[j-1]) 
	                    dp[j][i] = dp[j-1][i-1] + dp[j][i-1];
	                else dp[j][i] = dp[j][i-1];
	            }
	        }
	        
	        return dp[tLen][sLen];
	    }
	};