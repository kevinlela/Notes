### Longest Repeating Character Replacement
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

[leetcode](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

### Answer 
It is a two pointer problem, a window of width w only valid when the w - max(occurence of elements in window) <= k. Once the window is invalide, expanding becomes meaningless, so we shrink it until it is valid again. 

	class Solution {
	public:
	    int characterReplacement(string s, int k) {
	        // longest window with two distinct letter
	        vector<int> counts(26, 0);
	        
	        int sLen = s.size();
	        int st = 0, result = 0;
	        for (int i = 0; i < sLen; ++i)
	        {
	            ++counts[s[i] - 'A'];
	            int maxEle = getMax(counts);
	            if (i - st + 1 - maxEle > k) --counts[s[st++] - 'A'];
	            result = max(result, i - st + 1);
	        }
	        
	        return result;
	    }
	    
	    int getMax(const vector<int> &counts)
	    {
	        int result = 0;
	        for (int k = 0; k < counts.size(); ++k)
	        {
	            result = max(result, counts[k]);
	        }
	        return result;
	    }
	};