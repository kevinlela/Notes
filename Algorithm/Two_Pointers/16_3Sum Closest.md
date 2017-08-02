### 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

[leetcode](https://leetcode.com/problems/3sum-closest/description/)

### Answer:
Same as 3Sum problem [here](15_3Sum.md). 

	class Solution {
	public:
	    int threeSumClosest(vector<int>& nums, int target) {
	        if (nums.size() < 3) return -1;
	        
	        sort(nums.begin(), nums.end());
	        
	        int minDiff = -1, result = 0;
	        for (int i = 0; i < nums.size() - 2; )
	        {
	            int st = i + 1, ed = nums.size() - 1;
	            while (st < ed)
	            {
	                int sum = nums[i] + nums[st] + nums[ed];
	                int diff = sum - target;
	                int diffAbs = abs(diff);
	                
	                if (diff == 0) return sum;
	                if (minDiff > diffAbs || minDiff < 0)
	                {
	                    minDiff = diffAbs;
	                    result = sum;
	                }
	                
	                if (diff > 0) ed = findLeftNext(nums, ed);
	                else st = findRightNext(nums, st);
	            }
	            i = findRightNext(nums, i);
	        }
	        return result;
	    }
	    
	    int findRightNext(const vector<int> &nums, int st)
	    {
	        int currNum = nums[st++];
	        for (; st < nums.size(); ++st)
	        {
	            if (nums[st] != currNum) return st;
	        }
	        return st;
	    }
	    
	    int findLeftNext(const vector<int> &nums, int ed)
	    {
	        int currNum = nums[ed--];
	        for (; ed >= 0; --ed)
	        {
	            if (nums[ed] != currNum) return ed;
	        }
	        return ed;
	    }
	};