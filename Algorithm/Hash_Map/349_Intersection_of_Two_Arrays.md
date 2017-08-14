### Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

[leetcode](https://leetcode.com/problems/intersection-of-two-arrays/description/)

### Answer 

	class Solution {
	public:
	    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
	        unordered_set<int> s1(nums1.begin(), nums1.end());
	        vector<int> result;
	        for (auto iter = nums2.begin(); iter != nums2.end(); ++iter)
	        {
	            if (s1.find(*iter) != s1.end())
	            {
	                s1.erase(*iter);
	                result.push_back(*iter);
	            }
	        }
	        return result;
	    }
	};