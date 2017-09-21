### Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

[leetcode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)

### Answer
	class Solution {
	public:
	    int countComponents(int n, vector<pair<int, int>>& edges) {
	        vector<vector<int>> nei(n, vector<int> ());
	        vector<bool> visited(n, false);
	        for (int i = 0; i < edges.size(); ++i)
	        {
	            nei[edges[i].first].push_back(edges[i].second);
	            nei[edges[i].second].push_back(edges[i].first);
	        }
	        
	        int groups = 0;
	        for (int i = 0; i < n; ++i)
	        {
	            if (!visited[i])
	            {
	                dfs(nei, i, visited);
	                ++groups;
	            }
	        }
	        
	        return groups;
	    }
	    
	    void dfs(vector<vector<int>> &nei, int idx, vector<bool> &visited)
	    {
	        vector<int> &curr_nei = nei[idx];
	        visited[idx] = true;
	        
	        for (int i = 0; i < curr_nei.size(); ++i)
	        {
	            if (!visited[curr_nei[i]]) dfs(nei, curr_nei[i], visited);
	        }
	    }
	};