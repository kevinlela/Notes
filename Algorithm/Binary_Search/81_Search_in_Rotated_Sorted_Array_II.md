### Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

[leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/)

### Answer 

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.size() == 0) return false;
        int st = 0, ed = nums.size() - 1;
        while (st <= ed)
        {
            int mid = st + (ed - st) / 2;
            if (nums[mid] == target) return true;
            if (nums[mid] < target)
            {
                if (nums[mid] > nums[st]) st = mid + 1; // left is good
                else if (nums[mid] < nums[st])
                {
                    if (nums[ed] == nums[mid]) --ed;
                    else // (nums[ed] > nums[mid])
                    {
                        if (nums[ed] == target) return true;
                        else if (nums[ed] > target) st = mid + 1;
                        else ed = mid - 1;
                    }
                }
                else ++st;
            }
            else // nums[mid] > target
            {
                if (nums[mid] < nums[ed]) ed = mid - 1;
                else if (nums[mid] > nums[ed])
                {
                    if (nums[st] == nums[mid]) ++st;
                    else // (nums[st] < nums[mid])
                    {
                        if (nums[st] == target) return true;
                        else if (nums[st] < target) ed = mid - 1;
                        else st = mid + 1;
                    }
                }
                else --ed;
            }
            
        }
        return false;
    }
};