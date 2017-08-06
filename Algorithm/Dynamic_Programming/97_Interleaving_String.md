### Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

[leetcode](https://leetcode.com/problems/interleaving-string/description/)

### Answer 
define dp[i][j] as the whether s3[0, i+j] can be formed by s1[0...i] and s2[0...j]. dp[i][j] can choose either s1[i] or s2[j] as the last element. if none of them matches, it must be false. otherwise, if s1[i] match, dp[i][j] = dp[i-1][j] and vice versa.

	class Solution {
	public:
	    bool isInterleave(string s1, string s2, string s3) {
	        // dp[i][j] represent whether s1[1...i] and s2[1...j] can represent s3[1....i+j];
	        // dp[i][j] = (s3[i+j] == s1[i] & dp[i-1][j]) | (s3[i+j] == s2[j] & dp[i][j-1])
	        
	        int len1 = s1.size(), len2 = s2.size(), len3 = s3.size();
	        if (len1 + len2 != len3) return false;
	        
	        vector<vector<bool>> dp(len1 + 1, vector<bool> (len2 + 1, false));
	        dp[0][0] = true;
	        
	        for (int j = 1; j <= len1; ++j)
	        {
	            dp[j][0] = dp[j-1][0] & (s3[j-1] == s1[j-1]);
	        }
	        
	        for (int i = 1; i <= len2; ++i)
	        {
	            dp[0][i] = dp[0][i-1] & (s3[i-1] == s2[i-1]);
	        }
	        
	        for (int j = 1; j <= len1; ++j)
	        {
	            for (int i = 1; i <= len2; ++i)
	            {
	                dp[j][i] = (s3[i + j - 1] == s1[j-1] & dp[j-1][i])
	                          |(s3[i + j - 1] == s2[i-1] & dp[j][i-1]);
	            }
	        }
	        
	        return dp[len1][len2];
	    }
	};  