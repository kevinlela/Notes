### Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

[leetcode](https://leetcode.com/problems/search-insert-position/description/)

### Answer

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.empty()) return 0;
        int st = 0, ed = nums.size();
        if (nums[st] > target) return st;
        if (nums[ed -1] < target) return ed;
        
        while (st < ed)
        {
            int mid = st + (ed - st) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) ed = mid;
            else st = mid + 1;
        }
        
        return ed;
    }
};