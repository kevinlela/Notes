### Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

[leetcode](https://leetcode.com/problems/detect-capital/description/)

### Answer
	class Solution {
	public:
	    bool detectCapitalUse(string word) {
	        int len = word.size();
	        if (len == 0 || len == 1) return true;
	        bool isFirstCap = isupper(word[0]);
	        bool isSecCap = isupper(word[1]);
	        if (!isFirstCap && isSecCap) return false;
	        
	        for (int i = 2; i < len; ++i)
	        {
	            if (isFirstCap && isSecCap)
	            {
	                if(islower(word[i])) return false;
	            }
	            else if (isupper(word[i])) return false;
	        }
	        
	        return true;
	    }
	};