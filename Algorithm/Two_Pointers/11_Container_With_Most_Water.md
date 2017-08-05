### Container With Most Water

Given n non-negative integers a_1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

[leetcode](https://leetcode.com/problems/container-with-most-water/description/)

### Answer:
This is a tricky problem. if we have two bar A[i] and A[j]
if A[i] < A[j], that means fix A[i], any k between i and j will yield smaller value, so we perform ++i
else perform ++j

	class Solution {
	public:
	    int maxArea(vector<int>& height) {
	        // select two bars L and R
	        // if L > R, all the data between [L....R] and R will be less than the current result, so move R to left
	        // if R < L, oppositively, move L to right
	        if (height.size() < 2) return 0;
	        int st = 0, ed = height.size() -1, result = 0;
	        while (st < ed)
	        {
	            if (height[st] >= height[ed]) 
	            {
	                result = max(result, height[ed] * (ed - st));
	                --ed;
	            }
	            else
	            {
	                result = max(result, height[st] * (ed - st));
	                ++st;
	            }
	        }
	        return result;
	    }
	};
