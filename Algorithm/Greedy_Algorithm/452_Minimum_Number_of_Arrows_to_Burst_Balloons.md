### Minimum Number of Arrows to Burst Balloons
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

[leetcode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

### Answer
This problem is equal to what is the maximum disjoint event we can arrage in an array. After this, all the other unarranged events are overlaps with assigned ones. Break this optimal solution results in:

lose some interval -> need arrow to cover these intervals. This mean we can find more event to insert into the plan, this event does not overlap with any one so it must needs a arrow

	class Solution {
	public:
	    struct cmp{
	        inline bool operator() (const pair<int, int> &a, 
	                                const pair<int, int> &b)
	        {
	            return a.second < b.second;
	        }
	    };
	    
	    int findMinArrowShots(vector<pair<int, int>>& points) {
	        if (points.size() == 0) return 0;
	        
	        // scheduling problem
	        // since scheduling algorithm gives the max number of non-overlapping intervals, this means any other intervals should be overlaped with one of the chosen interval. this gives the minimum arrow needed
	        sort(points.begin(), points.end(), cmp());
	        
	        int result = 1;
	        int curr_ed = points[0].second;
	        
	        for (int i = 1; i < points.size(); ++i)
	        {
	            if (points[i].first <= curr_ed) continue;
	            else
	            {
	                ++result;
	                curr_ed = points[i].second;
	            }
	        }
	        
	        return result;
	    }
	};