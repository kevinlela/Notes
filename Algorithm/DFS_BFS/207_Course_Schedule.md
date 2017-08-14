### Course Schedule
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.

[leetcode](https://leetcode.com/problems/course-schedule/description/)

### Answer 
We can use DFS or BFS to do a topological sort. My solution is BFS. Calculate in edges and out edges for each node at each level, choose the one only with out edges and remove iteratively, until no such node exists. If all removed, then there is no circle otherwise, there is a circle. 

	class Solution {
	public:
	    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
	        vector<pair<int, int>> &p = prerequisites;
	        int n = numCourses, len = p.size();
	        
	        vector<vector<int>> nodes (n, vector<int>());
	        vector<int> inEdges(n, 0);
	        for (int i = 0; i < p.size(); ++i)
	        {
	            // in order to take first, need to take second
	            nodes[p[i].second].push_back(p[i].first);
	            ++inEdges[p[i].first];
	        }
	        
	        while (n)
	        {
	            int zeroIn = 0;
	            for (; zeroIn < numCourses; ++zeroIn)
	            {
	                if (inEdges[zeroIn] == 0) break;
	            }
	            if (zeroIn == numCourses) return false;
	            inEdges[zeroIn] = -1;
	            
	            vector<int> &curr = nodes[zeroIn];
	            for (int i = 0; i < curr.size(); ++i)
	            {
	                --inEdges[curr[i]];
	            }
	            --n;
	        }
	        
	        return true;
	    }
	};