### Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

[leetcode](https://leetcode.com/problems/graph-valid-tree/description/)

### Answer

A tree means no loop. so we can use DFS/BFS to traverse

	class Solution {
	public:
	    bool validTree(int n, vector<pair<int, int>>& edges) {
	        vector<bool> visited(n, false);
	        visited[0] = true;
	        vector<unordered_set<int>> nei(n, unordered_set<int>());
	        for (int i = 0; i < edges.size(); ++i)
	        {
	            nei[edges[i].first].insert(edges[i].second);
	            nei[edges[i].second].insert(edges[i].first);
	        }
	        
	        queue<int> q;
	        q.push(0);
	        
	        while (!q.empty())
	        {
	            int len = q.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int cand = q.front();
	                for (auto iter = nei[cand].begin(); iter != nei[cand].end(); ++iter)
	                {
	                    int curr_nei = *iter;
	                    if (visited[curr_nei]) return false;
	                    visited[curr_nei] = true;
	                    nei[curr_nei].erase(cand);
	                    q.push(curr_nei);
	                }
	                q.pop();
	            }
	        }
	        
	        for (int i = 0; i < n; ++i)
	        {
	            if (visited[i] == false) return false;
	        }
	        return true;
	    }
	};
