### Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

[leetcode](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

### Answer 

	class Solution {
	public:
	    string reverseVowels(string s) {
	        if  (s.empty()) return s;
	        int st = 0, ed = s.size() - 1;
	        while (st < ed)
	        {
	            while (st < ed && !isVowel(s[st])) ++st;
	            while (st < ed && !isVowel(s[ed])) --ed;
	            if (st < ed) swap(s[st++], s[ed--]);
	        }
	        
	        return s;
	    }
	    
	    bool isVowel(char c)
	    {
	        c = tolower(c);
	        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
	    }
	};