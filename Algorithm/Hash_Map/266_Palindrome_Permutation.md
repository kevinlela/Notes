### Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

[leetcode](https://leetcode.com/problems/palindrome-permutation/description/)

### Answer

	class Solution {
	public:
	    bool canPermutePalindrome(string s) {
	        // just need to count
	        unordered_map<char, int> count;
	        for (int i = 0; i < s.size(); ++i)
	            count[s[i]]++;
	        
	        int odd = 0;
	        for (auto iter = count.begin(); iter != count.end(); ++iter)
	        {
	            if (iter->second % 2 ) 
	            {
	                if (odd == 1) return false;
	                ++odd;
	            }
	        }
	        return true;
	    }
	};