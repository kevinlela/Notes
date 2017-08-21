### LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

[leetcode](https://leetcode.com/problems/lfu-cache/description/)

### Answer

Use list to record least frequency. like
            
            l4
            |
l3          l7
|           |
7 -> 6 ->   5 -> 4 ... -> 1

horizontally, record the frequencey, vertically record the recent used. 

When an key is get, delete it from the list and move forward..

	class LFUCache {
	public:
	    LFUCache(int capacity) {
	        d_capacity = capacity;
	    }
	    
	    int get(int key) {
	        if (data.find(key) == data.end()) return -1; // do not find
	        increment(key);
	        return data[key];
	    }
	    
	    void put(int key, int value) {
	        if (d_capacity == 0) return;
	        if (data.find(key) == data.end())
	        {
	            if (data.size() == d_capacity) deleteLF();
	            insertNew(key, value);
	        }
	        else
	        {
	            data[key] = value;
	            increment(key);
	        }
	    }
	    
	    void insertNew(int key, int value)
	    {
	        int key_freq = 1;
	        freq[key_freq].push_front(key);
	        pos[key].first = key_freq;
	        pos[key].second = freq[key_freq].begin();
	        data[key] = value;
	        min_freq = 1;
	    }
	    
	    void deleteLF()
	    {
	        int keyLF = *(freq[min_freq].rbegin());
	        data.erase(keyLF);
	        freq[min_freq].pop_back();
	        pos.erase(keyLF);
	        
	        // delete only happens when new element inserted 
	        // so the min_freq always becomes one in insert stage, so we do not update it here
	        if (freq[min_freq].size() == 0) 
	        {
	            freq.erase(min_freq);
	        }
	    }
	    
	    void increment(int key)
	    {
	        int key_freq = pos[key].first;
	        auto key_iter = pos[key].second;
	        
	        // update freq map
	        freq[key_freq].erase(key_iter);
	        if (freq[key_freq].size() == 0) 
	        {
	            freq.erase(key_freq);
	            if (key_freq == min_freq) ++min_freq;
	        }
	        freq[key_freq + 1].push_front(key); // the beginning means the most recent
	        
	        // update pos map
	        ++pos[key].first;
	        pos[key].second = freq[key_freq+1].begin();
	    }
	    
	private:
	    unordered_map<int, int> data;
	    unordered_map<int, list<int>> freq;
	    unordered_map<int, pair<int, list<int>::iterator> > pos; // <key, <freq_count, iter_in_freq>>
	    int min_freq;
	    int d_capacity;
	};

	/**
	 * Your LFUCache object will be instantiated and called as such:
	 * LFUCache obj = new LFUCache(capacity);
	 * int param_1 = obj.get(key);
	 * obj.put(key,value);
	 */
