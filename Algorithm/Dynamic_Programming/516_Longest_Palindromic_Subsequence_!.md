### Longest Palindromic Subsequence !
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

[leetcode](https://leetcode.com/problems/longest-palindromic-subsequence/description/)

### Answer
It is a dp problem. suppose dp[i][j] means the result of s[i...j]

dp[i][j] = max( dp[i+1][j-1] + s[j] == s[i] ? 2 : 0, 
				dp[i][j-1], 
				dp[i+1][j])

	class Solution {
	public:
	    int longestPalindromeSubseq(string s) {
	        //let dp[i][j] represent the max_len between s[i]...s[j]
	        // when s[j+1] comming, you want to measure dp[i][j+1], find all the first s[j+1] in i...j , say k, and dp[i][j+1] = dp[k][j] + 2;
	        int len = s.size();
	        vector<vector<int>> dp(len, vector<int>(len, 0));
	        int result = 0;
	        for (int i = 0; i < len; ++i)
	            dp[i][i] = 1;
	        
	        for (int i = 0, j = 1; i < len - 1; ++i, ++j)
	            dp[i][j] = s[i] == s[j] ? 2 : 1;
	        
	        for (int k = 2; k < len; ++k)
	        {
	            for (int i = 0, j = k; i < len - k; ++i, ++j)
	            {
	                if (s[j] == s[i])
	                    dp[i][j] = max(dp[i][j-1], dp[i+1][j-1] + 2);
	                else dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
	            }
	        }
	        
	        return dp[0][len-1];
	    }
	};
