### Best Meeting Point
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

[leetcode](https://leetcode.com/problemset/all/)

### Answer

	class Solution {
	public:
	    int minTotalDistance(vector<vector<int>>& grid) {
	        // dis = \sum |p_i(x) - m(x)| + \sum |p_j(y) - m(y)|
	        // the shortest point for each dimension is the middle point
	        vector<int> x;
	        vector<int> y;
	        for (int i = 0; i < grid.size(); ++i)
	        {
	            for (int j = 0; j < grid[i].size(); ++j)
	            {
	                if (grid[i][j])
	                {
	                    x.push_back(i);
	                    y.push_back(j);
	                }
	            }
	        }
	        
	        int len = x.size();
	        if (len <= 1) return 0;
	        
	        //sort(x.begin(), x.end());
	        sort(y.begin(), y.end());
	        
	        int m_x = 0, m_y = 0;
	        
	        m_x = x[(int)((len-1)/2)];
	        m_y = y[(int)((len-1)/2)];
	        
	        int result = 0;
	        for (int i = 0; i < x.size(); ++i)
	        {
	            result += abs(x[i] - m_x);
	            result += abs(y[i] - m_y);
	        }
	        return result;
	    }
	};