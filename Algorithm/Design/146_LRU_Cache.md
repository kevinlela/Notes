### LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

[leetcode](https://leetcode.com/problems/lru-cache/description/)

### Answer 

To enable the get by key, we need a hash map for sure to store every element. To enable the update frequence we need a list for O(1) delete and insert. So in the map, instead of storing the value, we can store the iterator in the linkedlist. 

	class LRUCache {
	public:
	    LRUCache(int capacity) : d_capacity(capacity){
	        
	    }
	    
	    int get(int key) {
	        if (d_keyListIter.find(key) == d_keyListIter.end()) return -1;
	        return updateKey(key, -1, false);
	    }
	    
	    void put(int key, int value) {
	        updateKey(key, value, true);
	    }
	    
	    int updateKey(int key, int value, bool updateValue)
	    {
	        if (!updateValue) value = d_keyListIter[key]->second;
	        
	        if (d_keyListIter.find(key) != d_keyListIter.end())
	            d_keyList.erase(d_keyListIter[key]);
	            
	        d_keyList.push_front({key, value});
	        d_keyListIter[key] = d_keyList.begin(); 
	        
	        if (d_keyList.size() > d_capacity)
	        {
	            int endKey = (d_keyList.rbegin())->first;
	            d_keyList.pop_back();
	            d_keyListIter.erase(endKey);
	        }
	        
	        return value;
	    }
	    
	private:
	    list<pair<int, int>> d_keyList; //left is the most recent, right is the least recent
	    unordered_map<int, list<pair<int, int>>::iterator> d_keyListIter;
	    int d_capacity;
	};

	/**
	 * Your LRUCache object will be instantiated and called as such:
	 * LRUCache obj = new LRUCache(capacity);
	 * int param_1 = obj.get(key);
	 * obj.put(key,value);
	 */