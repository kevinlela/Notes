### Insert Delete GetRandom O(1) - Duplicates allowed
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();


[leetcode](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/)

### Answer 
Extension to 380_Insert_Delete_GetRandom_O(1). Now we need store a map's map for the idx of each element. 

	class RandomizedCollection {
	public:
	    /** Initialize your data structure here. */
	    RandomizedCollection() {
	        
	    }
	    
	    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
	    bool insert(int val) {
	        bool result;
	        if (d_idx.find(val) == d_idx.end()) result = true;
	        else result = false;
	        int len = d_nums.size();
	        d_nums.push_back(val);
	        d_idx[val].insert(len);
	        return result;
	    }
	    
	    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
	    bool remove(int val) {
	        if (d_idx.find(val) == d_idx.end()) return false;
	        unordered_set<int> &target_idx = d_idx[val];
	        
	        auto iter = target_idx.begin();
	        int len = d_nums.size();
	        int last_item = *(d_nums.rbegin());
	        if (last_item == val)
	        {
	            d_nums.pop_back();
	            target_idx.erase(len-1);
	        }
	        else
	        {
	            d_idx[last_item].erase(len-1);
	            d_idx[last_item].insert(*iter);
	            d_nums[*iter] = last_item;
	            d_nums.pop_back();
	            target_idx.erase(*iter);
	        }
	        if (target_idx.empty()) d_idx.erase(val);
	        return true;
	    }
	    
	    /** Get a random element from the collection. */
	    int getRandom() {
	        int len = d_nums.size(); 
	        int ridx = rand()%len;
	        return d_nums[ridx];
	    }
	private:
	    vector<int> d_nums;
	    unordered_map<int, unordered_set<int>> d_idx;
	};

	/**
	 * Your RandomizedCollection object will be instantiated and called as such:
	 * RandomizedCollection obj = new RandomizedCollection();
	 * bool param_1 = obj.insert(val);
	 * bool param_2 = obj.remove(val);
	 * int param_3 = obj.getRandom();
	 */