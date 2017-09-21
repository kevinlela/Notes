### Design Snake Game
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

[leetcode](https://leetcode.com/problems/design-snake-game/description/)

### Answer

	class SnakeGame {
	public:
	    /** Initialize your data structure here.
	        @param width - screen width
	        @param height - screen height 
	        @param food - A list of food positions
	        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
	    SnakeGame(int width, int height, vector<pair<int, int>> food) {
	        d_w = width;
	        d_h = height;
	        d_score = 0;
	        d_food = food;
	        d_idx = 0;
	        d_snake.push({0, 0});
	        d_occ = vector<vector<bool>>(d_h, vector<bool>(d_w, false));
	        d_occ[0][0] = true;
	    }
	    
	    /** Moves the snake.
	        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
	        @return The game's score after the move. Return -1 if game over. 
	        Game over when snake crosses the screen boundary or bites its body. */
	    int move(string direction) {
	        if (d_score == -1) return d_score;
	        
	        pair<int, int> head = d_snake.back();
	        pair<int, int> tail = d_snake.front();
	        
	        if (direction == "U") --head.first;
	        else if (direction == "D") ++head.first;
	        else if (direction == "L") --head.second;
	        else if (direction == "R") ++head.second;
	        else 
	        {
	            d_score = -1;
	            return -1;
	        }
	        
	        if (head.first < 0 || head.first >= d_h || head.second < 0 || head.second >= d_w)
	        {
	            d_score = -1;
	            return -1;
	        }
	        
	        if (d_idx == d_food.size() || head != d_food[d_idx])
	        {
	            d_snake.pop();
	            d_occ[tail.first][tail.second] = false;
	        }
	        else
	        {
	            ++d_score;
	            ++d_idx;
	        }
	        
	        if (d_occ[head.first][head.second])
	        {
	            d_score = -1;
	            return d_score;
	        }
	        else d_occ[head.first][head.second] = true;
	        
	        d_snake.push(head);
	        
	        return d_score;
	    }
	    
	private:
	    vector<pair<int, int>> d_food;
	    int d_idx;
	    int d_w;
	    int d_h;
	    int d_score;
	    vector<vector<bool>> d_occ;
	    queue<pair<int, int>> d_snake;
	};

	/**
	 * Your SnakeGame object will be instantiated and called as such:
	 * SnakeGame obj = new SnakeGame(width, height, food);
	 * int param_1 = obj.move(direction);
	 */
