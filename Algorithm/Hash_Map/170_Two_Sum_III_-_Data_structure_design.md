### Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

[leetcode](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/)

### Answer
It depends on which operations are more, if we need to find more, we need to store all value of sum and sacrifice space complexity.

	class TwoSum {
	public:
	    /** Initialize your data structure here. */
	    TwoSum() {
	        
	    }
	    
	    /** Add the number to an internal data structure.. */
	    void add(int number) {
	        ++count[number];
	    }
	    
	    /** Find if there exists any pair of numbers which sum is equal to the value. */
	    bool find(int value) {
	        for (auto iter = count.begin(); iter != count.end(); ++iter)
	        {
	            int other = value - iter->first;
	            if (other == iter->first)
	            {
	                if (iter->second >= 2) return true;
	            }
	            else
	            {
	                if (count.find(other) != count.end()) return true;
	            }
	        }
	        return false;
	    }
	private:
	    unordered_map<int, int> count;
	};

	/**
	 * Your TwoSum object will be instantiated and called as such:
	 * TwoSum obj = new TwoSum();
	 * obj.add(number);
	 * bool param_2 = obj.find(value);
	 */