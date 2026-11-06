class Solution:
    def solve(self,ind,row,col,board,word,visited):
        if ind>=len(word)-1:
            return True
        
        if row-1>=0 and not visited[row-1][col] and board[row-1][col]==word[ind+1]:
            visited[row-1][col]=1
            flag=self.solve(ind+1,row-1,col,board,word,visited)
            visited[row-1][col]=0
            if flag:
                return True
        if row+1<len(board) and not visited[row+1][col] and board[row+1][col]==word[ind+1]:
            visited[row+1][col]=1
            flag=self.solve(ind+1,row+1,col,board,word,visited)
            visited[row+1][col]=0
            if flag:
                return True
        if col-1>=0 and not visited[row][col-1] and board[row][col-1]==word[ind+1]:
            visited[row][col-1]=1
            flag=self.solve(ind+1,row,col-1,board,word,visited)
            visited[row][col-1]=0
            if flag:
                return True
        if col+1<len(board[0]) and not visited[row][col+1] and board[row][col+1]==word[ind+1]:
            visited[row][col+1]=1
            flag=self.solve(ind+1,row,col+1,board,word,visited)
            visited[row][col+1]=0
            if flag:
                return True
        return False


    def exist(self, board: list[list[str]], word: str) -> bool:
        flag=False
        visited=[ [0]*len(board[0]) for _ in range(len(board)) ]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    visited[row][col]=1
                    if self.solve(0,row,col,board,word,visited):
                        return True
                    visited[row][col]=0
        return False
        