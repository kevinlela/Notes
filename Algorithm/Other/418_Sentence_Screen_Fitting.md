### Sentence Screen Fitting
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

[leetcode](https://leetcode.com/problems/sentence-screen-fitting/description/)

### Answer
use an idx to record, what is the number of word when starting at certain string. 

There is another extreme case: every row is quite short and the sentence is quite long, in this case, we'd better recore the number of rows for a sentence. 

	class Solution {
	public:
	    int wordsTyping(vector<string>& sentence, int rows, int cols) {
	        // initial check
	        for (int i = 0; i < sentence.size(); ++i)
	        {
	            if (sentence[i].size() > cols) return 0;
	        }
	        
	        vector<int> counts(sentence.size(), 0);
	        vector<int> edIdx(sentence.size(), 0);
	        int it = 0, idx = 0, result = 0;
	        while (it < rows)
	        {
	            if (counts[idx] == 0) 
	            {
	                fillRow(idx, cols, counts[idx], edIdx[idx], sentence);
	            }
	            result += counts[idx];
	            idx = edIdx[idx];
	            ++it;
	        }
	        
	        return result/(sentence.size());
	    }
	    
	    void fillRow(int idx, int cols, int &num, int &edIdx, vector<string> &s)
	    {
	        int curr_cols = 0;
	        while (curr_cols < cols)
	        {
	            if (curr_cols == 0) curr_cols += s[idx].size();
	            else
	            {
	                if (curr_cols + s[idx].size() + 1 > cols) break;
	                else curr_cols += s[idx].size() + 1;
	            }
	            ++idx;
	            if (idx == s.size()) idx = 0;
	            ++num;
	        }
	        
	        edIdx = idx;
	    }
	};
