### Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

[leetcode](https://leetcode.com/problems/insert-interval/description/)

### Answer 
Find the left boundary a[i].end < c[i].start, find the right boundary b[i].start > c[i].start, and merge everythig between a and b to c

	class Solution {
	public:
	    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
	        int left = 0, right = 0;
	        // find the right bound, can be log n
	        for (right = 0; right < intervals.size(); ++right)
	        {
	            if (newInterval.end < intervals[right].start) break;
	        }
	        
	        // find the left bound
	        for (left = right-1; left >= 0; --left)
	        {
	            if (newInterval.start > intervals[left].end) break;
	        }
	        
	        vector<Interval> result;
	        for (int i = 0; i <= left; ++i)
	        {
	            result.push_back(intervals[i]);
	        }
	        
	        for (int i = left + 1; i < right; ++i)
	        {
	            newInterval.start = min(newInterval.start, intervals[i].start);
	            newInterval.end = max(newInterval.end, intervals[i].end);
	        }
	        
	        result.push_back(newInterval);
	        
	        for (int i = right; i < intervals.size(); ++i)
	        {
	            result.push_back(intervals[i]);
	        }
	        
	        return result;
	    }
	};