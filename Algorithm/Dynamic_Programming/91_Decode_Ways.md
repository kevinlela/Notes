### Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

[leetcode](https://leetcode.com/problems/decode-ways/description/)

### Answer 
It is a dp problem but we need to take care of corner case like "02" or "27"

	class Solution {
	public:
	    int numDecodings(string s) {
	        if (s.size() == 0) return 0;
	        if (s[0] == '0') return 0;
	        int len = s.size();
	        vector<int> dp(len + 1, 0);
	        dp[1] = 1;
	        dp[0] = 1;
	        
	        for (int i = 2; i <= len; ++i)
	        {
	            if (s[i-1] != '0') dp[i] += dp[i-1];
	            int curr = (s[i-2] - '0')*10 + s[i-1] - '0';
	            if (s[i-2] != '0' && curr >= 10 && curr <= 26) dp[i] += dp[i-2];
	        }
	        
	        return dp[len];
	    }
	};

