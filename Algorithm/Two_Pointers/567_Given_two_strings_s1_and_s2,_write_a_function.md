### Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

[leetcode](https://leetcode.com/problems/permutation-in-string/description/)

### Answer
typical two pointers problem

	class Solution {
	public:
	    bool checkInclusion(string s1, string s2) {
	        // it is a two pointer problem
	        int st = 0;
	        int counts[26] = {0};
	        for (int i = 0; i < s1.size(); ++i)
	        {
	            ++counts[s1[i]-'a'];
	        }
	        int len = s1.size();
	        for (int i = 0; i < s2.size(); ++i)
	        {
	            if (counts[s2[i]-'a'] != 0)
	            {
	                --counts[s2[i]-'a'];
	                --len;
	                if (len == 0) return true;
	            }
	            else
	            {
	                for (st; st < i && s2[st] != s2[i]; ++st)
	                {
	                    ++counts[s2[st]-'a'];
	                    ++len;
	                }
	                ++st;
	            }
	        }
	        
	        return false;
	    }
	};