### Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

[leetcode](https://leetcode.com/problems/merge-sorted-array/description/)

### Answer 
Use the tail part of nums1 since it will touch the untouched value of nums1

	class Solution {
	public:
	    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
	        int len1 = nums1.size(), len2 = nums2.size();
	        int ed = len1 - 1;
	        int iter1 = m-1, iter2 = n-1;
	        
	        while (iter1 >= 0 || iter2 >= 0)
	        {
	            if (iter1 < 0) nums1[ed--] = nums2[iter2--];
	            else if (iter2 < 0) nums1[ed--] = nums1[iter1--];
	            else nums1[ed--] = nums1[iter1] > nums2[iter2] ? nums1[iter1--] : nums2[iter2--]; 
	        }
	        
	        int st = 0;
	        for (int i = len1 - m - n; i < len1; ++i)
	        {
	            nums1[st++] = nums1[i];
	        }
	    }
	};

