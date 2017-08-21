### Number of Boomerangs
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

[leetcode](https://leetcode.com/problems/number-of-boomerangs/description/)

### Answer
I use a quite brutal force idea with hashmap to decrease the complexity from O(N^3) to O(N^2)

	class Solution {
	public:
	    int numberOfBoomerangs(vector<pair<int, int>>& points) {
	        int len = points.size();
	        int count = 0;
	        for (int i = 0; i < len ; ++i)
	        {
	            unordered_map<int, int> dis_count;
	            for (int j = 0; j < len; ++j)
	            {
	                if (i == j) continue;
	                int dij = l2dis(points[i], points[j]);
	                ++dis_count[dij];
	            }
	            
	            for (auto iter = dis_count.begin(); iter != dis_count.end(); ++iter)
	            {
	                if (iter->second <= 1) continue;
	                count += iter->second * (iter->second - 1);
	            }
	        }
	        
	        return count;
	    }
	    
	    int l2dis(const pair<int, int> &p1, const pair<int, int> &p2)
	    {
	        return pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2);
	    }
	};
