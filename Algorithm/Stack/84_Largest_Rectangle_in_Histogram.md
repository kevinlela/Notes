### Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

[leetcode](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

### Answer 
This is a hard problem. 

What is the brutal force way. Choose all possible two bins and calculate the rec[i, j] = dis(i, j) * min(hist[i...j]) and result = max(rec[i, j]). Lead to O(N^2)

We need to detect the redundancy. 

if we have two bins i and j, any i <= k < j has hist[k] > hist[i], we conclude we can just use (j-k+1)*hist[j] to calculate, so they have no need to preserve. So, we can maintain a stack which has monotonically increased value. 

	class Solution {
	public:
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