### Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

[leetcode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

### Answer
Use array itself as a hash map

	class Solution {
	public:
	    vector<int> findDisappearedNumbers(vector<int>& nums) {
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
	            if (nums[i] - 1 != i) result.push_back(i + 1);
	        }
	        
	        return result;
	    }
	};
