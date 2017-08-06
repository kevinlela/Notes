### Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.


[leetcode](https://leetcode.com/problems/maximal-rectangle/description/)

### Answer 
Just an extention of [84](84_Largest_Rectangle_in_Histogram.md)

	class Solution {
	public:
	    int maximalRectangle(vector<vector<char>>& matrix) {
	        int h = matrix.size();
	        if (h == 0) return 0;
	        int w = matrix[0].size();
	        if (w == 0) return 0;
	        
	        vector<int> row(w, 0);
	        int maxArea = 0;
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                row[i] = matrix[j][i] == '0' ? 0 : row[i] + 1;
	            }
	            maxArea = max(maxArea, largestRectangleArea(row));
	        }
	        
	        return maxArea;
	    }
	    
	    int largestRectangleArea(vector<int>& heights) {
	        if (heights.size() == 0) return 0;
	        stack<int> stk;
	        stk.push(0);
	        int maxArea = 0;
	        for (int i = 1; i < heights.size(); ++i)
	        {
	            if (heights[i] < heights[stk.top()]) 
	            {
	                while (!stk.empty() && heights[stk.top()] > heights[i])
	                {
	                    int curr = stk.top();
	                    stk.pop();
	                    int prev = stk.empty() ? -1 : stk.top();
	                    maxArea = max(maxArea, heights[curr]*(i - prev - 1));
	                   
	                }
	            }
	            stk.push(i);
	        }
	        
	        int ed = (int)heights.size() - 1;
	        while (!stk.empty())
	        {
	            int curr = stk.top();
	            stk.pop();
	            int prev = stk.empty() ? -1 : stk.top();
	            maxArea = max(maxArea, (ed - prev) * heights[curr]);
	        }
	        
	        return maxArea;
	    }
	};