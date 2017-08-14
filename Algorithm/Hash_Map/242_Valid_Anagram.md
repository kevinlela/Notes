### Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

[leetcode](https://leetcode.com/problems/valid-anagram/description/)

### Answer 

	class Solution {
	public:
	    bool isAnagram(string s, string t) {
	        if (s.size() != t.size()) return false;
	        unordered_map<char, int> counts;
	        
	        for (int i = 0; i < s.size(); ++i)
	        {
	            ++counts[s[i]];
	        }
	        
	        for (int i = 0; i < t.size(); ++i)
	        {
	            --counts[t[i]];
	            if (counts[t[i]] < 0) return false;
	        }
	        
	        return true;
	    }
	};