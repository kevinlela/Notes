### Reverse Pairs
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

[leetcode](https://leetcode.com/problems/reverse-pairs/description/)

### Answer
* Store the nums[i] in map. and use lower bound. it will be O(N^2), search O(logN) and calculate distance to end O(N), iterate over N elements

* use merge sort O(NlogN)

* NOTICE !!!!, always consider merge sort if meed problem like i < j and num[i] ? nums[j]. Since in merge sort, we can immediately get position priori in each merge. 

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        // usually two methods
        // 1. use set and lower/upper (here lower) bound to find the element. but in this way, it is very hard to find the number of element. This method is more suitable to find existing or not
        // 2. use merge sort
        // both method has O(nlogn)
        int result = 0;
        int len = nums.size();
        mergeSort(nums, 0, len - 1, result);
        return result;
    }
    
    vector<int> mergeSort(const vector<int> &nums, int st, int ed, int &result)
    {
        if (st > ed) return vector<int> ();
        if (st == ed) return vector<int> (1, nums[st]);
        int mid = st + (ed - st) / 2;
        vector<int> left  = mergeSort(nums,     st, mid, result);
        vector<int> right = mergeSort(nums, mid + 1, ed, result);
        return merge(left, right, result);
    }
    
    vector<int> merge(const vector<int> &left, const vector<int> &right, int &result)
    {
        int mResNum = 0;
        vector<int> mRes = mergeHelp1(left, right);
        result += mergeHelp2(left, right);
        return mRes;
    }
    
    vector<int> mergeHelp1(const vector<int> &left, const vector<int> &right)
    {
        int iter1= 0, iter2 = 0, lenL = left.size(), lenR = right.size();
        vector<int> result;
        while (iter1 < lenL || iter2 < lenR)
        {
            if (iter2 == lenR) result.push_back(left[iter1++]);
            else if (iter1 == lenL) result.push_back(right[iter2++]);
            else if (left[iter1] > right[iter2]) result.push_back(left[iter1++]);
            else result.push_back(right[iter2++]);
        }
        return result;
    }
    
    int mergeHelp2(const vector<int> &left, const vector<int> &right)
    {
        int iter1= 0, iter2 = 0, lenL = left.size(), lenR = right.size();
        int numP = 0;
        while (iter1 < lenL || iter2 < lenR)
        {
            if (iter2 == lenR) ++iter1;
            else if (iter1 == lenL)
            {
                numP += iter1;
                ++iter2;
            }
            else if ((long)left[iter1] > ( (long)right[iter2] ) * 2) ++iter1;
            else 
            {
                numP += iter1;
                ++iter2;
            }
        }
        return numP;
    }
};




