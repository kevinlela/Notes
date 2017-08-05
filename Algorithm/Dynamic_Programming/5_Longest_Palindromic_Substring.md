### Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

	Input: "babad"

	Output: "bab"

Note: "aba" is also a valid answer.
Example:

	Input: "cbbd"

	Output: "bb"

[leetcode](https://leetcode.com/problems/longest-palindromic-substring/description/)

### Answer:

Traditional DP. let d[i][j] be whether a s[i...j] is a palindrome or not. Then, d[i][j+1] is palindrom if s[j+1] == s[i] && d[i+1][j] == true

	class Solution {
	public:
	    string longestPalindrome(string s) {
	        string result;
	        
	        if (s.empty())
	        {
	            return result;
	        }
	        
	        bool dp[1000][1000];
	        int maxLen = 0, st = 0;
	        
	        for (int i = 0; i < s.size(); ++i)
	        {
	            dp[i][i] = true;
	        }
	        
	        for (int i = 0, k = 1; i < s.size() -1 ; ++i)
	        {
	            int j = i + k;
	            dp[i][j] = (s[i] == s[j]);
	            if (dp[i][j])
	            {
	                maxLen = k;
	                st = i;
	            }
	        }
	        
	        for (int k = 2; k < s.size(); ++k)
	        {
	            for (int i = 0; i < s.size() - k; ++i)
	            {
	                int j = i + k;
	                dp[i][j] = dp[i+1][j-1] & (s[i] == s[j]);
	                if (dp[i][j])
	                {
	                    maxLen = k;
	                    st = i;
	                }
	            }
	        }
	            
	        return s.substr(st, maxLen + 1);
	    }
	};