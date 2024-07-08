"""
According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial
state: live (represented by a 1) or dead (represented by a 0). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the
current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""

import copy


class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        new_board = copy.deepcopy(board)
        # tl,tc,tr,cr,br,bc,bl,cl
        directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
        ]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                count = 0
                for dir in directions:
                    x = i + dir[0]
                    y = j + dir[1]
                    if x >= 0 and y >= 0 and x < m and y < n:
                        if board[x][y] == 1:
                            count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    new_board[i][j] = 0
                elif board[i][j] == 0 and count == 3:
                    new_board[i][j] = 1

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                board[i][j] = new_board[i][j]


if __name__ == "__main__":
    s = Solution()
    print(s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
