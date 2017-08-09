### Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

[leetcode](https://leetcode.com/submissions/detail/104185103/)

### Answer 
It is a bfs problem. One trick for this problem is that when we generate the next level of words, we can change very char. This is not an optimal solution as the complexity is 26*wordLen and traverse the map is numword. It is all depends on the test cases.

	class Solution {
	public:
	    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
	        unordered_set<string> cands;
	        for (int i = 0; i < wordList.size(); ++i)
	            cands.insert(wordList[i]);
	        if (cands.find(endWord) == cands.end()) return 0;
	        
	        queue<string> level;
	        cands.erase(beginWord);
	        level.push(beginWord);
	        
	        int result = 1;
	        while (!level.empty())
	        {
	            unordered_set<string> nextLevel;
	            int qLen = level.size();
	            for (int i = 0; i < qLen; ++i)
	            {
	                if (level.front() == endWord) return result;
	                getNextLevel(nextLevel, level.front(), cands);
	                level.pop();
	            }
	            
	            for (auto iter = nextLevel.begin(); iter != nextLevel.end();
	                      ++iter)
	            {
	                level.push(*iter);
	            }
	            ++result;
	        }
	        return 0;
	    }
	    
	    void getNextLevel(unordered_set<string> &nextlevel, 
	                      string &currWord, 
	                      unordered_set<string> &cands)
	    {
	        int len = currWord.size();
	        for (int i = 0; i < currWord.size(); ++i)
	        {
	            char tmp = currWord[i];
	            for (char j = 'a'; j <= 'z'; ++j)
	            {
	                if (j == tmp) continue;
	                currWord[i] = j;
	                if (cands.find(currWord) != cands.end())
	                {
	                    nextlevel.insert(currWord);
	                    cands.erase(currWord);
	                }
	            }
	            currWord[i] = tmp;
	        }
	    }
	};