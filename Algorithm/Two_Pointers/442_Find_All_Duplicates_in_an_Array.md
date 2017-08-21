### Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

[leetcode](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)

### Answer
This is two-pointer (swap) + use the array itself as hash map

	class Solution {
	public:
	    vector<int> findDuplicates(vector<int>& nums) {
	        //use the array as hash map
	        int len = nums.size();
	        int st = 0, ed = len - 1;
	        
	        vector<int> result;
	        while (1)
	        {
	            while (ed >= 0 && st <= ed && nums[ed]-1 == ed)
	            {
	                --ed;
	            }
	            
	            if (st > ed) break;
	            
	            int curr = nums[st]; // target index curr - 1;
	            if (st == curr - 1) 
	            {
	                ++st;
	                continue; // very good , keep going on
	            }
	            else
	            {
	                if (nums[curr - 1] == curr) //happen twice
	                {
	                    swap(nums[st], nums[ed--]); //swap with the safe entry
	                }
	                else
	                {
	                    swap(nums[st], nums[curr - 1]);
	                }
	            }
	        }
	        
	        for (int i = 0; i < len; ++i)
	        {
	            if (nums[i] - 1 != i) result.push_back(nums[i]);
	        }
	        
	        return result;
	    }
	};