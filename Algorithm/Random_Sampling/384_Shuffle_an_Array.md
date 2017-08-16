### Shuffle an Array
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

[leetcode](https://leetcode.com/problems/shuffle-an-array/description/)

### Answer 
Yates_Shuffeling
	class Solution {
	public:
	    Solution(vector<int> nums) {
	        d_nums = nums;
	        d_ori = nums;
	    }
	    
	    /** Resets the array to its original configuration and return it. */
	    vector<int> reset() {
	        d_nums = d_ori;
	        return d_nums;
	    }
	    
	    /** Returns a random shuffling of the array. */
	    vector<int> shuffle() {
	        int len = d_nums.size();
	        for (int i = 0; i < len; ++i)
	        {
	            swap(d_nums[i], d_nums[i + rand() % (len - i)]);
	        }
	        return d_nums;
	    }
	private:
	    vector<int> d_nums;
	    vector<int> d_ori;
	};

	/**
	 * Your Solution object will be instantiated and called as such:
	 * Solution obj = new Solution(nums);
	 * vector<int> param_1 = obj.reset();
	 * vector<int> param_2 = obj.shuffle();
	 */