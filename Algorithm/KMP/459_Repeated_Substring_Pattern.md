### Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False

Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

[leetcode](https://leetcode.com/problems/repeated-substring-pattern/description/)

### Answer
KMP

	class Solution {
	public:
	    bool repeatedSubstringPattern(string s) {
	        if (s.size() == 0) return 0;
	        int len = s.size();
	        vector<int> kmp (len, 0);
	        int j = 0;
	        for (int i = 1; i < len; ++i)
	        {
	            if (s[i] == s[j]) kmp[i] = (j++) + 1;
	            else
	            {
	                j = i;
	                while (j)
	                {
	                    j = kmp[j-1];
	                    if (s[j] == s[i]) 
	                    {
	                        kmp[i] = (j++) + 1;
	                        break;
	                    }
	                }
	            }
	        }
	        
	        return kmp[len - 1] != 0 && len % (len - kmp[len - 1]) == 0;
	    }
	};
