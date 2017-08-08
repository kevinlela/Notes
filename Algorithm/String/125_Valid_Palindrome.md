### Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

[leetcode](https://leetcode.com/problems/valid-palindrome/description/)

### Answer 
	class Solution {
	public:
	    bool isPalindrome(string s) {
	        int len = s.size();
	        int st = 0, ed = len - 1;
	        
	        while (st < ed)
	        {
	            if (isalnum(s[st]) == false) ++st;
	            else if (isalnum(s[ed]) == false) --ed;
	            else if (tolower(s[st++]) != tolower(s[ed--])) return false;
	        }
	        
	        return true;
	    }
	};