### Longest Substring with At Most Two Distinct Characters
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.

[leetcode](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)

### Answer
We can optimize the solution by using an array with size 2

	class Solution {
	public:
	    int lengthOfLongestSubstringTwoDistinct(string s) {
	        int st = 0, ed = 0, maxLen = 0;
	        unordered_map<char, int> count;
	        
	        for (int i = 0; i < s.size(); ++i, ++ed)
	        {
	            count[s[i]]++;
	            if (count.size() > 2)
	            {
	                maxLen = max(maxLen, ed - st);
	                while (count.size() > 2)
	                {
	                    count[s[st]]--;
	                    if (count[s[st]] == 0) count.erase(s[st]);
	                    ++st;
	                }
	            }
	        }
	        maxLen = max(maxLen, ed - st);
	        return maxLen;
	    }
	};