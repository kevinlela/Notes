Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

### Answer:

Record every appeared element a[i] and target - a[i] to find a[j]

	class Solution {
	public:
	    vector<int> twoSum(vector<int>& nums, int target) {
	        unordered_map<int, int> existed;
	        vector<int> result;
	        for (int i = 0; i != nums.size(); ++i)
	        {
	            int remain = target - nums[i];
	            if (existed.find(remain) == existed.end())
	            {
	                existed[nums[i]] = i;
	            }
	            else
	            {
	                result.push_back(existed[remain]);
	                result.push_back(i);
	                return result;
	            }
	        }
	        return result;
	    }
	};