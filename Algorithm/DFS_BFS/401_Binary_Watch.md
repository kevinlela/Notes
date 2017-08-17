### Binary Watch
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

[leetcode](https://leetcode.com/problems/binary-watch/description/)

### Answer 

	class Solution {
	public:
	    vector<string> readBinaryWatch(int num) {
	        vector<string> result;
	        for (int i = 0; i <= 4; ++i)
	        {
	            int j = num - i;
	            vector<int> hrs;
	            recur(hrs, 0, i, 0, 11, 4);
	            if (hrs.size() == 0) continue;
	            vector<int> mins;
	            recur(mins, 0, j, 0, 59, 7);
	            if (mins.size() == 0) continue;
	            for (int n = 0; n < hrs.size(); ++n)
	            {
	                for (int m = 0; m < mins.size(); ++m)
	                {
	                    result.push_back(to_string(hrs[n]) + ":" + (mins[m] < 10 ? "0" : "") 
	                                   + to_string(mins[m]));
	                }
	            }
	        }
	        return result;
	    }
	    
	    void recur(vector<int> &result, int curr, int counts, int idx, 
	               int maxVal, int maxIdx)
	    {
	        if (curr > maxVal || idx > maxIdx) return;
	        if (counts == 0)
	        {
	            result.push_back(curr);
	            return;
	        }
	        
	        recur(result, curr,            counts,     idx + 1, maxVal, maxIdx);
	        recur(result, curr | (1<<idx), counts - 1, idx + 1, maxVal, maxIdx);
	    }
	};