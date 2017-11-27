### Find the Difference
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.


[leetcode](https://leetcode.com/problems/find-the-difference/description/)

### Answer 

	class Solution {
	public:
	    char findTheDifference(string s, string t) {
	        int counts[26] = {0};
	        for (int i = 0; i < s.size(); ++i)
	        {
	            ++counts[s[i]-'a'];
	        }
	        
	        for (int i = 0; i < t.size(); ++i)
	        {
	            --counts[t[i]-'a'];
	            if (counts[t[i]-'a'] < 0) return t[i];
	        }
	        
	        return 0;
	    }
	};