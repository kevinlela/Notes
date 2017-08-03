### Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

[leetcode](https://leetcode.com/problems/next-permutation/description/)

### Answer

What is next permutation? from the end to the first, detect and pos with x[i] < x[i+1], Then, exchange the element with the first larger element after it. 

	class Solution {
	public:
	    void nextPermutation(vector<int>& nums) {
	        if (nums.size() <= 1) return;
	        int i = 0;
	        for (i = nums.size() - 1; i >= 1; --i)
	        {
	            if (nums[i - 1] < nums[i]) break;
	        }
	        
	        if (i == 0) 
	        {
	            reverse(nums.begin(), nums.end());
	            return;
	        }
	        
	        int target = i - 1;
	        for (i = nums.size() - 1; i >= 1; --i)
	        {
	            if (nums[i] > nums[target]) break;
	        }
	        
	        swap(nums[i], nums[target]);
	        reverse(nums.begin() + (target + 1), nums.end());
	        return;
	    }
	};