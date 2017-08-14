### Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

[leetcode](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

### Answer 

	class Solution {
	public:
	    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
	        unordered_map<int, int> s1;
	        for (auto iter = nums1.begin(); iter != nums1.end(); ++iter)
	        {
	            ++s1[*iter];
	        }
	        
	        vector<int> result;
	        for (auto iter = nums2.begin(); iter != nums2.end(); ++iter)
	        {
	            auto target = s1.find(*iter);
	            if (target == s1.end()) continue;
	            if (target->second == 0) continue;
	            --target->second;
	            result.push_back(*iter);
	        }
	        
	        return result;
	    }
	};