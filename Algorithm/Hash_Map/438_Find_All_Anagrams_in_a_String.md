### Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

[leetcode](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

### Answer
it is a hash map + fix window size problem. always count the new element and erase the oldest element. 

	class Solution {
	public:
	    vector<int> findAnagrams(string s, string p) {
	        vector<int> result;
	        if (p.empty()) return result;
	        
	        unordered_map<int, int> win;
	        for (int i = 0; i < p.size(); ++i)
	        {
	            ++win[p[i]];
	        }
	        int len = p.size(), count = 0;
	    
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (i >= len && win.find(s[i-len]) != win.end())
	            {
	                ++win[s[i-len]];
	                if (win[s[i-len]] == 0) ++count;
	                else if (win[s[i-len]] == 1) --count;
	            }
	            
	            if (win.find(s[i]) != win.end())
	            {
	                --win[s[i]];
	                if (win[s[i]] == 0) ++count;
	                else if (win[s[i]] == -1) --count;
	                if (count == win.size())
	                {
	                    result.push_back(i - len + 1);
	                }
	            }
	        }
	        
	        return result;
	    }
	};
