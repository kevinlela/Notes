### Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

[leetcode](https://leetcode.com/problems/keyboard-row/description/)

### Answer

	class Solution {
	public:
	    vector<string> findWords(vector<string>& words) {
	        unordered_set<char> r1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'};
	        unordered_set<char> r2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l' };
	        unordered_set<char> r3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm' };
	        
	        vector<string> result;
	        for (int i = 0; i < words.size(); ++i)
	        {
	            if (isInRow(words[i], r1) ||
	                isInRow(words[i], r2) ||
	                isInRow(words[i], r3))
	            {
	                result.push_back(words[i]);
	            }
	        }
	        
	        return result;
	    }
	    
	    bool isInRow(const string &word, const unordered_set<char> &r)
	    {
	        for (int i =0; i < word.size(); ++i)
	        {
	            if (r.find(tolower(word[i])) == r.end()) return false;
	        }
	        return true;
	    }
	};
