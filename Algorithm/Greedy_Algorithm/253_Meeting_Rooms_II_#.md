### Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

[leetcode](https://leetcode.com/problems/meeting-rooms-ii/description/)

### Answer
It is a greedy algorithm, first, for one room, we rank the intervals by end time and for the room, we always find the recent end room. 

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
	    struct cmp{
	        inline bool operator() (Interval &a, Interval &b)
	        {
	            if (a.end == b.end) return a.start < b.start;
	            return a.end < b.end;
	        }
	    };
	    
	    int minMeetingRooms(vector<Interval>& intervals) {
	        if (intervals.size() == 0) return 0;
	        sort(intervals.begin(), intervals.end(), cmp());
	        multiset<int, std::greater<int>> allEnds;
	        for (int i = 0; i < intervals.size(); ++i)
	        {
	            auto iter = allEnds.lower_bound(intervals[i].start);
	            if (iter != allEnds.end()) allEnds.erase(iter);
	            allEnds.insert(intervals[i].end);
	        }
	        return allEnds.size();
	    }
	};