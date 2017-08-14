### Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

[leetcode](https://leetcode.com/problems/range-sum-query-immutable/description/)

### Answer 

	class NumArray {
	public:
	    NumArray(vector<int> nums) {
	        int sum = 0;
	        d_sum.push_back(0);
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            sum += nums[i];
	            d_sum.push_back(sum);
	        }
	    }
	    
	    int sumRange(int i, int j) {
	        return d_sum[j+1] - d_sum[i];
	    }
	    
	private:
	    vector<int> d_sum;
	};

	/**
	 * Your NumArray object will be instantiated and called as such:
	 * NumArray obj = new NumArray(nums);
	 * int param_1 = obj.sumRange(i,j);
	 */