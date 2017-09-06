### Delete Operation for Two Strings
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

[leetcode](https://leetcode.com/problems/delete-operation-for-two-strings/description/)

### Answer
It is a dp problem. use dp[i][j] to represent the result of s1[0...i] and s2[0...j]

	class Solution {
	public:
	    int minDistance(string word1, string word2) {
	        int len1 = word1.size(), len2 = word2.size();
	        vector<vector<int>> dp(len1 + 1, vector<int> (len2 + 1, 0));
	        
	        for (int i = 0; i <= len2; ++i)
	            dp[0][i] = i;
	        for (int i = 0; i <= len1; ++i)
	            dp[i][0] = i;
	        
	        for (int i = 1; i <= len1; ++i)
	        {
	            for (int j = 1; j <= len2; ++j)
	            {
	                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1;
	                if (word1[i-1] == word2[j-1]) dp[i][j] = min(dp[i][j], dp[i-1][j-1]);
	            }
	        }
	        
	        return dp[len1][len2];
	    }
	};