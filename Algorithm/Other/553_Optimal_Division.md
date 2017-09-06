### Optimal Division
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.

[leetcode](https://leetcode.com/problems/optimal-division/description/)

### Answer

This is a dumb tricky problem. 

a1/(a2/a3 ... an) = a1*a3*...an / a2 will always gives largest result.

	class Solution {
	public:
	    string optimalDivision(vector<int>& nums) {
	        //this problem is interesting, it requires analysis in advance
	        //you can always use merge or dfs to solve this kind of paranthesis problem, but this one has optimal solution.
	        //when we meet x1/x2/x3.../xn, the maximum value should be x1*x3*x4*xn / x2
	        //if the input is not integer, the above ones does not valid
	        int len = nums.size();
	        if (len == 0) return "";
	        if (len == 1) return to_string(nums[0]);
	        if (len == 2) return to_string(nums[0]) + "/" + to_string(nums[1]);
	        string result = to_string(nums[0]) + "/(" + to_string(nums[1]);
	        for (int i = 2; i < len; ++i)
	        {
	            result += "/" + to_string(nums[i]);
	        }
	        result += ")";
	        return result;
	    }
	};
