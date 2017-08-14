### Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

[leetcode](https://leetcode.com/problems/course-schedule-ii/description/)

### Answer 
Same as [207](207_Course Schedule.md). BFS is more suitable to print out the path. 

	class Solution {
	public:
	    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
	        vector<vector<int>> nodes(numCourses, vector<int>());
	        vector<int> inEdges(numCourses, 0);
	        vector<pair<int, int>> &p = prerequisites;
	        for (int k = 0; k < p.size(); ++k)
	        {
	            nodes[p[k].second].push_back(p[k].first);
	            ++inEdges[p[k].first];
	        }
	        
	        int n = numCourses;
	        vector<int> result;
	        while (n)
	        {
	            int target = 0;
	            for (; target < numCourses; ++target)
	            {
	                if(inEdges[target] == 0) break;
	            }
	            if (target == numCourses) return vector<int>();
	            result.push_back(target);
	            for (int k = 0; k < nodes[target].size(); ++k)
	            {
	                --inEdges[nodes[target][k]];
	            }
	            inEdges[target] = -1;
	            --n;
	        }
	        
	        return result;
	    }
	};