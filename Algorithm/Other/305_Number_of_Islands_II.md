### Number of Islands II
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

[leetcode](https://leetcode.com/problems/number-of-islands-ii/description/)

### Answer
	class Solution {
	public:
	    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
	        if (n == 0 || m == 0) return vector<int> ();
	        vector<vector<int>> label(m, vector<int>(n, -1));
	        vector<int> result;
	        for (int i = 0; i < positions.size(); ++i)
	        {
	            addLand(positions[i], label);
	            result.push_back(d_num_label);
	        }
	        return result;
	    }
	    
	    void addLand(pair<int, int> &p, vector<vector<int>> &label)
	    {
	        int h = label.size(), w = label[0].size();
	        int c = p.second, r = p.first;
	        if (c < 0 || r < 0 || c >= w || r>= h) return;
	        if (label[r][c] != -1) return;
	        // check nei
	        unordered_set<int> neiLabel;
	        if (c - 1 >= 0 && label[r][c-1] != -1) neiLabel.insert(label[r][c-1]);
	        if (c + 1 <  w && label[r][c+1] != -1) neiLabel.insert(label[r][c+1]);
	        if (r - 1 >= 0 && label[r-1][c] != -1) neiLabel.insert(label[r-1][c]);
	        if (r + 1 <  h && label[r+1][c] != -1) neiLabel.insert(label[r+1][c]);
	        
	        if (neiLabel.empty()) //single island, create new island
	        {
	            int l = d_label_parent.size();
	            d_label_parent.push_back(l);
	            label[r][c] = l;
	            d_num_label += 1;
	        }
	        else 
	        {
	            unordered_set<int> roots;
	            for (auto it = neiLabel.begin(); it != neiLabel.end(); ++it)
	            {
	                roots.insert(findRoot(*it));
	            }
	            if (roots.size() == 1) // assign into the island
	            {
	                int l = *neiLabel.begin();
	                label[r][c] = l;
	            }
	            else
	            {
	                auto rit = roots.begin();
	                int l = *(rit++);
	                label[r][c] = l;
	                for (rit; rit != roots.end(); ++rit)
	                    d_label_parent[*rit] = l;
	                d_num_label -= roots.size() - 1;
	            }
	        }
	    }
	    
	    int findRoot(int child)
	    {
	        while (1)
	        {
	            int parent = d_label_parent[child];
	            if (parent == child) return parent;
	            child = parent;
	        }
	        return -1;
	    }
	    
	private:
	    vector<int> d_label_parent;
	    int d_num_label;
	};