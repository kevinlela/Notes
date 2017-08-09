### Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

[leetcode](https://leetcode.com/problems/palindrome-partitioning/description/)

### Answer 

Use dp[i][j] to represent if s[i...j] is parlinedrome, so we the parlindrome detection becomes O(N^2) frp, O(N^3). To all possibility, it is a backtracking (dfs) problem

	class Solution {
	public:
	    vector<vector<string>> partition(string s) {
	        int len = s.size();
	        vector<vector<string>> result;
	        if (len == 0) return result;
	        vector<string> path;
	        
	        vector<vector<bool>> dp = parlindromeDP(s);
	 
	        recur(result, path, s, 0, dp);
	        return result;
	    }
	    
	    void recur(vector<vector<string>> &result, vector<string> &path, const string &s, int curr,
	               const vector<vector<bool>> &dp)
	    {
	        int len = s.size();
	        if (curr >= len)
	        {
	            result.push_back(path);
	            return;
	        }
	        
	        for (int i = 1; curr + i <= len; ++i)
	        {
	            if (dp[curr][curr + i - 1])
	            {
	                path.push_back(s.substr(curr, i));
	                recur(result, path, s, curr + i, dp);
	                path.pop_back();
	            }
	        }
	    }
	    
	    vector<vector<bool>> parlindromeDP(const string &s)
	    {
	        // the result dp reprent whether s[j ... i] is a parlindrome or not
	        int len = s.size();
	        vector<vector<bool>> dp(len, vector<bool>(len, false));
	        
	        for (int j = 0; j < len; ++j)
	        {
	            dp[j][j] = true;
	        }
	        
	        for (int j = 0; j < len-1; ++j)
	        {
	            dp[j][j+1] = (s[j] == s[j+1]);
	        }
	        
	        for (int k = 2; k < len; ++k)
	        {
	            for (int j = 0, i = k; j < len - k; ++j, ++i)
	            {
	                dp[j][i] = dp[j+1][i-1] && (s[j] == s[i]);
	            }
	        }
	        
	        return dp;
	    }
	};