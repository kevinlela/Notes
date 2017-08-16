### Insert Delete GetRandom O(1)
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

[leetcode](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)

### Answer 
To random get out an element, the best container is vector. However, vector cannot get O(1) remove, So we use a map to record the val, find the value by using map and swap it with the last item and pop it out. 

	class RandomizedSet {
	public:
	    /** Initialize your data structure here. */
	    RandomizedSet() {
	        
	    }
	    
	    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
	    bool insert(int val) {
	        if (d_idx.find(val) != d_idx.end()) return false;
	        int n = d_val.size();
	        d_val.push_back(val);
	        d_idx[val] = n;
	        return true;
	    }
	    
	    /** Removes a value from the set. Returns true if the set contained the specified element. */
	    bool remove(int val) {
	        if (d_idx.find(val) == d_idx.end()) return false;
	        int ed_val = *d_val.rbegin();
	        if (ed_val == val)
	        {
	            d_val.pop_back();
	            d_idx.erase(val);
	            return true;
	        }
	        int target_idx = d_idx[val];
	        d_val[target_idx] = ed_val;
	        d_idx[ed_val] = target_idx;
	        d_val.pop_back();
	        d_idx.erase(val);
	        return true;
	    }
	    
	    /** Get a random element from the set. */
	    int getRandom() {
	        int n = d_val.size();
	        if (n == 0) return -1;
	        return d_val[rand() % n];
	    }
	private:
	    unordered_map<int, int> d_idx;
	    vector<int> d_val;
	};

	/**
	 * Your RandomizedSet object will be instantiated and called as such:
	 * RandomizedSet obj = new RandomizedSet();
	 * bool param_1 = obj.insert(val);
	 * bool param_2 = obj.remove(val);
	 * int param_3 = obj.getRandom();
	 */