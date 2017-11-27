### Wiggle Sort II @
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

[leetcode](https://leetcode.com/problems/wiggle-sort-ii/description/)

### Answer 
	Small half:  M . M . S . S      Small half:  M . S . S . S .
	Large half:  . L . L . M .      Large half:  . L . M . M . M
	--------------------------      --------------------------
	Together:    M L M L S M S      Together:    M L S M S M S M
	
	class Solution {
	public:
	    void wiggleSort(vector<int>& nums) {
	        vector<int> s(nums.begin(), nums.end());
	        sort(s.begin(), s.end(), greater<int>());
	        int len = s.size();
	        int mid = len / 2, st = 0, i = 0, mid_flag = mid;
	        while (1)
	        {
	            if (mid < len) nums[i++] = s[mid++];
	            if (mid_flag == st) break;
	            nums[i++] = s[st++];
	            
	        }
	    }
	};