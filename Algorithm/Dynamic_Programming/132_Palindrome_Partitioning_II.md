### Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

[leetcode](https://leetcode.com/problems/palindrome-partitioning-ii/description/)

### Answer 
This is a dp problem. First, we need could use dp to determine parlindrome for all subsequence. let dp[i] represents the minimum cut for s[0..i]. For s[i+1], we find all possible parlindrome between s[0...i] and dp[i+1] = min(1 + dp[k]) if s[k+1...i_1] is a parlindrome. Complexity O(N^2)

	class Solution {
	public:
	    int minCut(string s) {
	        int len = s.size();
	        if (len == 0) return 0;
	        vector<vector<bool>> dpPar = parlindromeDP(s);
	        vector<int> dpCut(len, 0);
	        dpCut[0] = 0;
	        
	        for (int j = 1; j < len; ++j)
	        {
	            if (dpPar[0][j]) dpCut[j] = 0; //the whole string is a parlindrome
	            else 
	            {
	                dpCut[j] = dpCut[j-1];   
	                for (int i = 0; i < j-1; ++i)
	                {
	                    if (dpPar[i+1][j]) dpCut[j] = min(dpCut[i], dpCut[j]);
	                }
	                dpCut[j] += 1; //add a cut after target i
	            }
	            //cout << dpCut[j] << endl;
	        }
	        
	        return dpCut[len-1];
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