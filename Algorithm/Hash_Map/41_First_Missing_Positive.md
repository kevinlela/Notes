### First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

[leetcode](https://leetcode.com/problems/first-missing-positive/description/)

### Answer 

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        // use the array index as hash table
        // when nums[index] == index: get it
        if (nums.size() == 0) return 1;
        int len = nums.size();
        
        int st = 0, ed = nums.size() - 1;
        
        while (st <= ed)
        {
            if (nums[st] == st + 1) ++st;
            else if (nums[st] > len || nums[st] < 1) swap(nums[st], nums[ed--]);
            else if (nums[nums[st] - 1] == nums[st]) swap(nums[st], nums[ed--]);
            else swap(nums[st], nums[nums[st]-1]);
        }
        
        return st + 1;
    }
};