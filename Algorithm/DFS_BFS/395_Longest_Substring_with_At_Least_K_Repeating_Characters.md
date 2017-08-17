### Longest Substring with At Least K Repeating Characters
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

[leetcode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/)

### Answer 
The delimeter is the string less than k times , we divide these intervals and check them one by one. 

	class Solution {
	public:
	    int longestSubstring(string s, int k) {
	        int len = s.size();
	        return recur(s, 0, len - 1, k);
	    }
	    
	    int recur(const string &s, int st, int ed, int k)
	    {
	        if (st > ed) return 0;
	        int counts[26] = {0};
	        for (int i = st; i <= ed; ++i)
	        {
	            ++counts[s[i] - 'a'];
	        }
	        
	        int result = 0, prev = st;
	        for (int i = st; i <= ed; ++i)
	        {
	            if (counts[s[i] - 'a'] < k) 
	            {
	                result = max(result, recur(s, prev, i - 1, k));
	                prev = i + 1;
	            }
	        }
	        if (prev == st) return ed - st + 1;
	        return max(result, recur(s, prev, ed, k));
	    }
	};