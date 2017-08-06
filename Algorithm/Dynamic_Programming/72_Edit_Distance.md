### Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

[leetcode](https://leetcode.com/problems/edit-distance/description/)

### Answer 

suppose dp[i][j] means the edit distance of word1[0...i] and word2[0...j]

four operation, insert word2[j], delete word1[i], replace word1[i] with word2[j], do nothing

	class Solution {
	public:
	    int minDistance(string word1, string word2) {
	        // let dp[j][i] means word1[0...i] match word2[0...j]
	        // insert word2[j]: dp[j-1][i]
	        // delete word1[i]: dp[j][i-1]
	        // replace word1[i]: dp[j-1][i-1]
	        
	        int len1 = word1.size(), len2 = word2.size();
	        vector<vector<int>> dp(len2 + 1, vector<int>(len1 + 1, 0));
	        
	        for (int i = 1; i <= len1; ++i)
	        {
	            dp[0][i] = i;
	        }
	        
	        for (int j = 1; j <= len2; ++j)
	        {
	            dp[j][0] = j;
	        }
	        
	        for (int j = 1; j <= len2; ++j)
	        {
	            for (int i = 1; i <= len1; ++i)
	            {
	                dp[j][i] = min(dp[j-1][i-1] + (word1[i-1] == word2[j-1] ? 0 : 1), min(dp[j-1][i], dp[j][i-1]) + 1);
	            }
	        }
	        
	        return dp[len2][len1];
	    }
	};