### Generalized Abbreviation
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

[leetcode](https://leetcode.com/problems/generalized-abbreviation/description/)

### Answer
	class Solution {
	public:
	    vector<string> generateAbbreviations(string word) {
	        vector<string> result;
	        word.push_back('#');
	        recur(word, word.size() - 1, result);
	        return result;
	    }
	    
	    void recur(string word, int idx, vector<string> &result)
	    {
	        if (idx < 0)
	        {
	            word.pop_back();
	            result.push_back(word);
	            return;
	        }
	        
	        int count = 0;
	        string tail = word.substr(idx); // prevent the first letter to be ommitted
	        string head = word.substr(0, idx);
	        // omit nothing
	        recur(head + tail, idx - 1, result); 
	        
	        for (int i = idx - 1; i >= 0; --i)
	        {
	            head.pop_back();
	            recur(head + to_string(++count) + tail, i - 1, result);
	        }
	    }
	};