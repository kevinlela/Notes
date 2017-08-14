### Minimum Height Trees
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

[leetcode](https://leetcode.com/problems/minimum-height-trees/description/)

### Answer 
This is a tricky problem. The simplest way to me is to prune leaves layer by layer. The theory behind it is that we need to keet each branch as uniform as possible. This is like a BFS but from leaf

	class Solution {
	public:
	    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
	        // bfs remove from outside
	        vector<unordered_set<int>> nodes(n, unordered_set<int>());
	        
	        for (int i = 0; i < edges.size(); ++i)
	        {
	            nodes[edges[i].first].insert(edges[i].second);
	            nodes[edges[i].second].insert(edges[i].first);
	        }
	        
	        queue<int> myQ;
	        for (int i = 0; i < n; ++i)
	        {
	            if (nodes[i].size() <= 1) myQ.push(i);
	        }
	        
	        if (nodes.size() == 1 || nodes.size() == 2) return checkout(myQ);
	        int totalNum = n;
	        
	        while (1)
	        {
	            int len = myQ.size();
	            totalNum -= myQ.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int curr = myQ.front();
	                myQ.pop();
	                for (auto iter = nodes[curr].begin(); iter != nodes[curr].end(); ++iter)
	                {
	                    nodes[*iter].erase(curr);
	                    if (nodes[*iter].size() == 1) myQ.push(*iter);
	                }
	            }
	            if (totalNum - myQ.size() == 0) break;
	        }
	        
	        return checkout(myQ);
	    }
	    
	    vector<int> checkout(queue<int> &myQ)
	    {
	        vector<int> result;
	        while (!myQ.empty())
	        {
	            result.push_back(myQ.front());
	            myQ.pop();
	        }
	        return result;
	    }
	};