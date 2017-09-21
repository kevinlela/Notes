### Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

[leetcode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)

### Answer
	class Solution {
	public:
	    int lengthOfLongestSubstringKDistinct(string s, int k) {
	        if (k == 0) return 0;
	        int st = 0, result = 0;
	        unordered_map<char, int> win;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (win.size() < k || win.find(s[i]) != win.end()) ++win[s[i]];
	            else // need to insert new char
	            {
	                for (st; st < i; ++st) // pop one old char
	                {
	                    --win[s[st]];
	                    if (win[s[st]] == 0)
	                    {
	                        win.erase(win.find(s[st++]));
	                        break;
	                    }
	                }
	                ++win[s[i]];
	            }
	            result = max(result, i - st + 1);
	        }
	        
	        return result;
	    }
	};