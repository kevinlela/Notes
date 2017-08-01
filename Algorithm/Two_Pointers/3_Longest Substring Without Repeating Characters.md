### Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

{https://leetcode.com/problems/longest-substring-without-repeating-characters/description/}

### Answer:

maintain a window contains unique chars as [st, ed], when ed + 1 invalidate the window, that means there is a st <= t <= ed where A[ed + 1] == A[t], all the window between [st, ed + 1] - [t, ed + 1] is invalid. The thinking process of two pointer problem is always maintaining a valid window. 

	class Solution {
	public:
	    int lengthOfLongestSubstring(string s) {
	        unordered_set<char> win;
	        int maxLen = 0, currLen = 0;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (win.find(s[i]) == win.end())
	            {
	                win.insert(s[i]);
	                ++currLen;
	            }
	            else
	            {
	                int st = i - currLen;
	                for (; st < i; ++st, --currLen)
	                {
	                    if (s[st] == s[i])
	                    {
	                        break;
	                    }
	                    win.erase(s[st]);
	                }
	            }
	            maxLen = max(maxLen, currLen);
	        }
	        return maxLen;
	    }
	};