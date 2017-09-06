### Minimum Time Difference
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

[leetcode](https://leetcode.com/problems/minimum-time-difference/description/)

### Answer
Sort the time in nlogn

	class Solution {
	public:
	    struct less_than{
	        inline bool operator() (const pair<int, int> &p1, 
	                                const pair<int, int> &p2)
	        {
	            if (p1.first == p2.first) return p1.second < p2.second;
	            return p1.first < p2.first;
	        }
	    };
	    int findMinDifference(vector<string>& timePoints) {
	        vector<pair<int, int>> allTime;
	        int len = timePoints.size();
	        for (int i = 0; i < len; ++i)
	        {
	            allTime.push_back(parseTime(timePoints[i]));
	        }
	        sort(allTime.begin(), allTime.end(), less_than());
	        
	        int minDiff = INT_MAX;
	        for (int i = 0; i < len; ++i)
	        {
	            int resDiff = i == 0 ? diff(allTime[len-1], allTime[i]) :
	                                diff(allTime[i-1], allTime[i]);
	            minDiff = min(minDiff, resDiff);
	            if (minDiff == 0) return minDiff;
	        }
	        return minDiff;
	    }
	    
	    int diff(const pair<int, int> &p1, const pair<int, int> &p2)
	    {
	        int result = 0;
	        if (p2.first < p1.first) result = (p2.first + 24 - p1.first) * 60;
	        else result = (p2.first - p1.first) * 60;
	        result += p2.second - p1.second;
	        return abs(result);
	    }
	    
	    pair<int, int> parseTime(const string &t)
	    {
	        return {atoi(t.substr(0, 2).c_str()), atoi(t.substr(3, 2).c_str())};
	    }
	};