### Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

[leetcode](https://leetcode.com/problems/subarray-sum-equals-k/description/)

### Answer

Use hash map to store sum[i]

	class Solution {
	public:
	    int subarraySum(vector<int>& nums, int k) {
	        // notice here, it is integer include negative value
	        // brutal force is O(N^2)
	        // can improve to O(nlogn) by using multiset
	        // actually, we do not need multiset, we need multimap
	        int sum = 0, result = 0;
	        unordered_map<int, int> umap;
	        umap[0] = 1;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            sum += nums[i];
	            if (umap.find(sum - k) != umap.end()) result += umap[sum - k];   
	            ++umap[sum];
	        }
	        return result;
	    }
	};
