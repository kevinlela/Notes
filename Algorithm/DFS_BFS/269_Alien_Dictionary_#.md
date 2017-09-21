### Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

[leetcode](https://leetcode.com/problems/alien-dictionary/description/)

### Answer
This is a very good example of using topological sort

	class Solution {
	public:
	    string alienOrder(vector<string>& words) {
	        // It is a topological sorting problem
	        unordered_map<char, unordered_set<char>> edges;
	        constructGraph(words, edges);
	        return topoSort(edges);
	    }
	    
	    string topoSort(unordered_map<char, unordered_set<char>> &edges)
	    {
	        string result;
	        unordered_map<char, int> inEdges;
	        for (auto it = edges.begin(); it != edges.end(); ++it)
	        {
	            if (inEdges.find(it->first) == inEdges.end())
	                inEdges[it->first] = 0;
	            for (auto it2 = it->second.begin(); it2 != it->second.end(); ++it2)
	            {
	                ++inEdges[*it2];
	            }
	        }
	        
	        unordered_map<char, int>::iterator it;
	        while (!inEdges.empty())
	        {
	            for (it = inEdges.begin(); it != inEdges.end(); ++it)
	            {
	                if (it->second == 0) break;
	            }
	            if (it == inEdges.end()) return "";
	            result.push_back(it->first);
	            auto target = edges.find(it->first);
	            for (auto neiIt = target->second.begin(); neiIt != target->second.end(); ++neiIt)
	            {
	                --inEdges[*neiIt];
	            }
	            inEdges.erase(it);
	        }
	        
	        return result;
	    }
	    
	    void constructGraph(const vector<string> &words, unordered_map<char, unordered_set<char>> &edges)
	    {
	        for (int i = 0; i < words.size(); ++i)
	        {
	            bool alreadyFind = false;
	            for (int j = 0; j < words[i].size(); ++j)
	            {
	                if (edges.find(words[i][j]) == edges.end())
	                    edges[words[i][j]] = unordered_set<char>();
	                if (i == 0) continue;
	                if (!alreadyFind && j < words[i-1].size())
	                {
	                    if (words[i][j] != words[i-1][j])
	                    {
	                        edges[words[i-1][j]].insert(words[i][j]);
	                        alreadyFind = true;
	                    }
	                }
	            }
	        }
	    }
	};