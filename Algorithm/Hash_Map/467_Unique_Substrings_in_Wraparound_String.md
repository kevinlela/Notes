### Unique Substrings in Wraparound String
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

[leetcode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/)

### Answer

* first of all, if we detect consecutive segment in p, we can know all its substring

* how to detect distinct ones, we can fix the first char and use hash map to track

* for now, the complexity is O(N^2)

* Do we need to recalculate? say, we detect z, a, b, c, d. we done for z but do we need to do another rought for a? no, we just use len_z - 1 for a. For hashmap, we just need to record the maximum number. of each char.

* So every element will only be visited twice. So the complexity if O(N)

	class Solution {
	public:
	    int findSubstringInWraproundString(string p) {
	        vector<int> counts(26, 0);
	        int len = p.size(); // first of all, the single char must be a choice
	        //find consecutive substring
	        int prev = 0, count = 0, result = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            int diff = (int)p[i] - prev;
	            if (diff == 1 || (p[i] == 'a' && prev == 'z')) ++count;
	            else count = 1;
	            counts[p[i] - 'a'] = max(counts[p[i] - 'a'], count);
	            prev = p[i];
	        }  
	        
	        for (int i =0 ; i < 26; ++i)
	        {
	            result += counts[i];
	        }
	        
	        return result;
	    }
	};
