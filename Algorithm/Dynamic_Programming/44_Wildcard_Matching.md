### Wildcard Matching
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "*") ? true
isMatch("aa", "a*") ? true
isMatch("ab", "?*") ? true
isMatch("aab", "c*a*b") ? false

[leetcode](https://leetcode.com/problems/wildcard-matching/description/)

### Answer 
Similar to [Regular Expression Matching]{10_Regular_Expression_Matching.md}

	class Solution {
	public:
	    bool isMatch(string s, string p) {
	        // * enable three operation, delete and insert and replacement
	        // ? enable replacement
	        
	        // dp[i][j] means s[0...i] matches p[0...j]
	        //      if (p[j] == '?') d[i][j] = d[i-1][j-1]
	        // else if (p[j] == '*') d[i][j] = d[i][j-1] (empty) || d[i-1][j-1] (replacement) || d[i-1][j] (insert)
	        //                  else d[i][j] = d[i-1][j-1] && s[i] == p[j]
	        
	        // consecutive * means nothing, shrink it to single to reduce complexity
	        p = shrinkStar(p);
	        
	        int pLen = p.size(), sLen = s.size();
	        
	        vector<vector<bool>> dp(sLen + 1, vector<bool> (pLen + 1, false));
	        
	        dp[0][0] = true;
	        
	        for (int j = 1; j <= pLen; ++j)
	        {
	            if (p[j-1] == '*') dp[0][j] = dp[0][j-1];
	        }
	        
	        for (int i = 1; i <= sLen; ++i)
	        {
	            for (int j = 1; j <= pLen; ++j)
	            {
	                if (p[j-1] == '?') dp[i][j] = dp[i-1][j-1];
	                else if (p[j-1] == '*') dp[i][j] = dp[i][j-1] || dp[i-1][j-1] || dp[i-1][j];
	                else dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1]);
	            }
	        }
	        
	        return dp[sLen][pLen];
	    }
	    
	    string shrinkStar(const string &inStr)
	    {
	        string result;
	        if (inStr.size() == 0) return result;
	        result += inStr[0];
	        
	        for (int i = 1; i < inStr.size(); ++i)
	        {
	            if (*(result.rbegin()) == '*' && inStr[i] == '*') continue;
	            result += inStr[i];
	        }
	        return result;
	    }
	};