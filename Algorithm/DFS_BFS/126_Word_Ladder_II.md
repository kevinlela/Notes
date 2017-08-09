### Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

[leetcode](https://leetcode.com/problems/word-ladder-ii/description/)

### Answer 
Since it needs shortest path so bfs is more suitable

	class Solution {
	public:
	    struct WordNode {
	        WordNode(const string *wordIn) : word(wordIn), parent(NULL) {}
	        const string *word;
	        vector<WordNode*> parent;
	    };
	    
	    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
	        // it is more like dps problem
	        // it is my first thought because I did not see it requires us to find the shortest transformation
	        // so we need to use bfs to solve this problem
	        vector<vector<string>> result;
	        
	        unordered_set<WordNode*> wordNodesSet;
	        vector<WordNode*> wordGraph;
	        WordNode *beginNode = new WordNode(&beginWord), 
	                 *endNode = NULL;
	                 
	        wordGraph.push_back(beginNode);
	        wordNodesSet.insert(beginNode);
	        
	        int len = wordList.size();
	        for (int i = 0; i < len; ++i)
	        {
	            WordNode *node = new WordNode(&wordList[i]);
	            wordGraph.push_back(node);
	            wordNodesSet.insert(node);
	            if (endWord == wordList[i]) endNode = node;
	        }
	        
	        // there is a fucking case the endNode is not int the word list
	        if (endNode == NULL) return result;
	    
	        // start bfs
	        queue<WordNode*> cands;
	        cands.push(beginNode);
	        wordNodesSet.erase(beginNode);
	        
	        while (!cands.empty())
	        {
	            int qLen = cands.size();
	            
	            // add next layer
	            unordered_set<WordNode*> nextLayer;
	            for (int i = 0; i < qLen; ++i)
	            {
	                WordNode* curr = cands.front();
	                for (auto iter = wordNodesSet.begin(); 
	                          iter != wordNodesSet.end();
	                          ++iter)
	                {
	                    if (isLadder((*iter)->word, curr->word))
	                    {
	                        if (nextLayer.find(*iter) == nextLayer.end())
	                            nextLayer.insert(*iter);
	                        (*iter)->parent.push_back(curr);
	                    }
	                }
	                cands.pop();
	            }
	            
	            // erase next layer in graph and add it into the queue
	            bool findLast = false;
	            for (auto iter = nextLayer.begin(); 
	                      iter != nextLayer.end(); ++iter)
	            {
	                if (*iter == endNode)
	                {
	                    findLast = true;
	                    break;
	                }
	                cands.push(*iter);
	                wordNodesSet.erase(*iter);
	            }
	            
	            if (findLast) break;
	        }
	        
	        // backtrack to get the shortest path
	        vector<string> path;
	        path.push_back(*(endNode->word));
	        trackBack(result, path, endNode, beginNode);
	        
	        // release the graph
	        for (int i = 0; i < wordGraph.size(); ++i)
	        {
	            delete wordGraph[i];
	        }
	        
	        return result;
	    }
	    
	    void trackBack(vector<vector<string>> &result, 
	                   vector<string> &path, WordNode* prev, 
	                   WordNode *beginNode)
	    {
	        if (prev == beginNode)
	        {
	            reverse(path.begin(), path.end());
	            result.push_back(path);
	            reverse(path.begin(), path.end());
	            return;
	        }
	        
	        for (auto iter = prev->parent.begin(); iter != prev->parent.end();
	                  ++iter)
	        {
	            //cout << *((*iter)->word) << endl;
	            path.push_back(*((*iter)->word));
	            trackBack(result, path, *iter, beginNode);
	            path.pop_back();
	        }
	    }
	    
	    bool isLadder(const string *s1, const string *s2)
	    {
	        int len = s1->size();
	        bool count = false;
	        for (int i = 0; i < len; ++i)
	        {
	            if ((*s1)[i] != (*s2)[i])
	            {
	                if (count) return false;
	                else count = true;
	            }
	        }
	        return true;
	    }
	};