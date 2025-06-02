class Solution:
    '''
    TC: O(m*n)
    AS: O(1)
    '''

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) #rows
        n = len(board[0]) #columns

        for i in range(m):
            for j in range(n):
                countAlives = self.countALives(board, i, j)
                
                # Rule 1 & Rule 3 -> combining over-population and under-population
                if board[i][j] == 1  and  (countAlives < 2 or countAlives > 3):
                    board[i][j] = 5

                # Rule 2 - redundant ; live cell stays live

                # Rule 4 
                if board[i][j] == 0  and  countAlives == 3:
                    board[i][j] = 4


        for i in range(m):
            for j in range(n):
                
                # Live(1) to Dead(0) --> 5
                if board[i][j] == 5:
                    board[i][j] = 0
                
                # Dead(0) to Live(1) --> 4
                if board[i][j] == 4:
                    board[i][j] = 1


    def countALives(self, board, r, c):
        # Neighbors in the direction array
        #      R      L        U       D     upright  upleft  downright downleft
        dirs = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (-1, -1), (1, 1), (1, -1)]
        result = 0 # total number of lives around the cell

        for dir in dirs:
            nr = r + dir[0]
            nc = c + dir[1]

        # check bounds -> check if valid
            # m = len(board) #rows
            # n = len(board[0]) #columns
            if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]) and (board[nr][nc] == 1 or board[nr][nc] == 5):
                result += 1

        return result
            