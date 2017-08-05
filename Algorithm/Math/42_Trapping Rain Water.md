### Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

[leetcode](https://leetcode.com/problems/trapping-rain-water/description/)

### Answer 

This is a very tricky problem. for each bin, we just need to find what the water it can hold. Because this amount only depends on the left largest and right largest bin. 

	class Solution {
	public:
	    int trap(vector<int>& height) {
	        vector<int> leftMax(height.size(), 0);
	        for (int i = 0, prev = 0; i < height.size(); ++i)
	        {
	            leftMax[i] = prev;
	            prev = max(prev, height[i]);
	        }
	        
	        vector<int> rightMax(height.size(), 0);
	        for (int i = height.size(), prev = 0; i > 0; )
	        {
	            --i;
	            rightMax[i] = prev;
	            prev = max(prev, height[i]);
	        }
	        
	        int result = 0;
	        for (int i = 0; i < height.size(); ++i)
	        {
	            int diff = min(leftMax[i], rightMax[i]) - height[i];
	            result += diff > 0 ? diff : 0;
	        }
	        
	        return result;
	    }
	};