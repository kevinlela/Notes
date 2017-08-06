### Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

[leetcode](https://leetcode.com/problems/merge-intervals/description/)

### Answer 

1) sort the array by starting point
2) merge interval

	/**
	 * Definition for an interval.
	 * struct Interval {
	 *     int start;
	 *     int end;
	 *     Interval() : start(0), end(0) {}
	 *     Interval(int s, int e) : start(s), end(e) {}
	 * };
	 */
	class Solution {
	public:
	    struct IntervalCmp{
	        bool operator () (Interval &a, Interval &b)
	        {
	            return a.start == b.start ? a.end < b.end : a.start < b.start;
	        }
	    };

	    vector<Interval> merge(vector<Interval>& intervals) {
	        // first, we need to sort the intervals by the starting time
	        sort(intervals.begin(), intervals.end(), IntervalCmp());
	        
	        if (intervals.size() <= 1) return intervals;
	        
	        vector<Interval> result;
	        result.push_back(intervals[0]);
	        
	        for (int i = 1; i < intervals.size(); ++i)
	        {
	            if (intervals[i].start <= result.rbegin()->end)
	            {
	                result.rbegin()->end = max(result.rbegin()->end, intervals[i].end);
	            }
	            else result.push_back(intervals[i]);
	        }
	        
	        return result;
	    }
	};