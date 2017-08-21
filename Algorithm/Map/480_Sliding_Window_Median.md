### Sliding Window Median
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

[leetcode](https://leetcode.com/problems/sliding-window-median/description/)

### Answer
Use two sets to track the window O(Nlogk)

	class Solution {
	public:
	    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
	        MedianFilter mf(k);
	        vector<double> result;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            mf.insert(nums[i]);
	            if (i < k - 1) continue;
	            result.push_back(mf.getMedian());
	        }
	        return result;
	    }
	private:
	    class MedianFilter{
	    public:
	        MedianFilter(int capacity) : d_capacity(capacity) {}
	        
	        double getMedian()
	        {
	            if (d_left.size() > d_right.size()) return *d_left.begin();
	            double l = *d_left.begin();
	            double r = *d_right.begin();
	            return (l + r) / 2;
	        }
	        
	        void insert(int num)
	        {
	            if (d_win.size() == d_capacity) 
	            {
	                maintainWin();
	            }
	            d_win.push(num);
	            
	            if (num < *d_left.begin()) d_left.insert(num);
	            else d_right.insert(num);
	            balanceTwo();
	        }
	        
	        void balanceTwo()
	        {
	            if (d_left.size() == d_right.size()) return;
	            if (d_left.size() == d_right.size() + 1) return;
	            if (d_left.size() > d_right.size())
	            {
	                while (1)
	                {
	                    int num = *d_left.begin();
	                    d_left.erase(d_left.begin());
	                    d_right.insert(num);
	                    if (d_left.size() == d_right.size()) return;
	                    if (d_left.size() == d_right.size() + 1) return;
	                }
	            }
	            else
	            {
	                while (1)
	                {
	                    int num = *d_right.begin();
	                    d_right.erase(d_right.begin());
	                    d_left.insert(num);
	                    if (d_left.size() == d_right.size()) return;
	                    if (d_left.size() == d_right.size() + 1) return;
	                }
	            }
	        }
	        
	        void maintainWin()
	        {
	            auto liter = d_left.find(d_win.front());
	            if (liter != d_left.end())
	            {
	                d_left.erase(liter);
	                d_win.pop();
	                return;
	            }
	            
	            auto riter = d_right.find(d_win.front());
	            if (riter != d_right.end())
	            {
	                d_right.erase(riter);
	                d_win.pop();
	                return;
	            }
	        }
	        
	    private:
	        multiset<int, greater<int>> d_left;
	        multiset<int> d_right;
	        queue<int> d_win;
	        int d_capacity;
	    };
	};


