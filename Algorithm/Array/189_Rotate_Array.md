### Rotate Array
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?

[leetcode](https://leetcode.com/problems/rotate-array/description/)

### Answer 

	class Solution {
	public:
	    void rotate(vector<int>& nums, int k) {
	        int len = nums.size();
	        if (len <= 1) return;
	        k %= len;
	        if (k == 0) return;
	        
	        reverse(nums.begin(), nums.end());
	        reverse(nums.begin(), nums.begin() + k);
	        reverse(nums.begin() + k, nums.end());
	        
	        return;
	    }
	};