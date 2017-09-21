### Shortest Word Distance III
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.

[leetcode](https://leetcode.com/problems/shortest-word-distance-iii/description/)

### Answer
	class Solution {
	public:
	    int shortestWordDistance(vector<string>& words, string word1, string word2) {
	        int idx1 = -1, idx2 = -1;
	        int result = INT_MAX;
	        if (word1 == word2)
	        {
	            for (int i = 0; i < words.size(); ++i)
	            {
	                if (words[i] == word1)
	                {
	                    if (idx1 != -1)
	                    {
	                        result = min(result, i - idx1);
	                    }
	                    idx1 = i;
	                }
	            }
	        }
	        else
	        {
	            for (int i = 0; i < words.size(); ++i)
	            {
	                if (words[i] == word1)
	                {
	                    idx1 = i;
	                }
	                else if (words[i] == word2)
	                {
	                    idx2 = i;
	                }
	                if (idx1 != -1 && idx2 != -1)
	                {
	                    result = min(abs(idx1 - idx2), result);
	                }
	            }
	        }
	        
	        return result;
	    }
	};