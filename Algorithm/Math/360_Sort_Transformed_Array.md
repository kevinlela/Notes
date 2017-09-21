### Sort Transformed Array
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]

[leetcode](https://leetcode.com/problems/sort-transformed-array/description/)

### Answer
Need to consider corner case, a == 0 and b < 0

    class Solution {
    public:
        vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
            if (nums.size() == 0) return {};
            double peek = a == 0 ? (b < 0 ? nums[nums.size() - 1] : nums[0]) : (-(double)b/2/(double)a);
            int st = 0, ed = nums.size();
            while (st < ed)
            {
                int mid = st + (ed - st)/2;
                if (nums[mid] <= peek) st = mid+1;
                else ed = mid;
            }
            cout << ed << endl;
            int iter2 = ed, iter1 = ed - 1;
            vector<int> result;
            while (iter2 < nums.size() || iter1 >= 0)
            {
                if (iter2 >= nums.size()) result.push_back(a*nums[iter1]*nums[iter1] + b*nums[iter1--] + c);
                else if (iter1 < 0) result.push_back(a*nums[iter2]*nums[iter2] + b*nums[iter2++] + c);
                else
                {
                    int res1 = a*nums[iter1]*nums[iter1] + b*nums[iter1] + c;
                    int res2 = a*nums[iter2]*nums[iter2] + b*nums[iter2] + c;
                    if (a < 0)
                    {
                        if (res1 > res2)
                        {
                            result.push_back(res1);
                            --iter1;
                        }
                        else
                        {
                            result.push_back(res2);
                            ++iter2;
                        }
                    }
                    else
                    {
                        if (res1 < res2)
                        {
                            result.push_back(res1);
                            --iter1;
                        }
                        else
                        {
                            result.push_back(res2);
                            ++iter2;
                        }
                    }
                    
                }
            }
            
            if (a < 0) reverse(result.begin(), result.end());
            
            return result;
        }
        
    };