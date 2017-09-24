### Valid Word Abbreviation
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.

[leetcode](https://leetcode.com/problems/valid-word-abbreviation/description/)

### Answer
	class Solution {
	public:
	    bool validWordAbbreviation(string word, string abbr) {
	        int len = word.size();
	        int jump = 0, j = 0;
	        word += " ";
	        abbr += " ";
	        string digit;
	        for (int i = 0; i < abbr.size(); ++i)
	        {
	            if (isdigit(abbr[i]))
	            {
	                if (digit.empty() && abbr[i] == '0') return false;
	                digit.append(1, abbr[i]);
	            }
	            else
	            {
	                jump = digit.empty() ? 0 : atoi(digit.c_str());
	                if (j + jump > len) return false;
	                if (word[j + jump] != abbr[i]) return false;
	                j += jump + 1;
	                digit = "";
	            }
	        }
	        return j == len + 1;
	    }
	};