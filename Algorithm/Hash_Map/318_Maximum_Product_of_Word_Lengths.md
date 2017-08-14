### Maximum Product of Word Lengths
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

[leetcode](https://leetcode.com/problems/maximum-product-of-word-lengths/description/)

### Answer 
We can use bitmap to store each word. 

	class Solution {
	public:
	    int maxProduct(vector<string>& words) {
	        int len = words.size();
	        vector<int> nums(len, 0);
	        for (int i = 0; i < len; ++i)
	        {
	            for (int j = 0; j < words[i].size(); ++j)
	            {
	                nums[i] |= 1<<(words[i][j]-'a');
	            }
	        }
	        
	        int result = 0;
	        for (int j = 0; j < len; ++j)
	        {
	            for (int i = j + 1; i < len; ++i)
	            {
	                if ( (nums[j]&nums[i]) == 0) 
	                {
	                    int len1 = words[j].size(), len2 = words[i].size();
	                    result = max(result, len1 * len2);
	                }
	            }
	        }
	        
	        return result;
	    }
	};