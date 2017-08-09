### Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

[leetcode](https://leetcode.com/problems/gas-station/description/)

### Answer 
It is a greedy algorithm, The state of a station is indepent to the starting traverse points. We randomly start from a pos, keep going to right (clock-wise).If the tank becomes negative. we need to add station to its left to guarantee that it has sufficient tank to arrive at this station. 

	class Solution {
	public:
	    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
	        int len = gas.size();
	        if (len == 0) return -1;
	        
	        int st = 0, ed = 0;
	        int sum = gas[0] - cost[0];
	        
	        if (len == 1) return sum < 0 ? -1 : 0;
	        
	        do
	        {
	            if (sum < 0)
	            {
	                if (st == 0) st = len - 1;
	                else --st;
	                sum += gas[st] - cost[st];
	            }
	            else
	            {
	                if (ed == len - 1) ed = 0;
	                else ++ed;
	                sum += gas[ed] - cost[ed];
	            }
	        }while (st != ed);
	        
	        return sum < 0 ? -1 : st;
	    }
	};