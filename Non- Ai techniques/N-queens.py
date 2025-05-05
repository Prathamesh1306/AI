def is_safe(board,n,row,col):
    for i in range(row):  # for row
         if board[i][col]==1:
              return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)): # for diagonal
         if board[i][j]==1:
              return False
    for i,j in zip(range(row,-1,-1),range(col,n)):  # for column
         if board[i][j]==1:
              return False
         
    return True

def solve_queen(board,n,row):
     if row>=n:
          return True
     
     for col in range(n):
          if is_safe(board,n,row,col):
               board[row][col]=1

               if solve_queen(board,n,row+1):
                    return True
               
               board[row][col]=0

     return False

def print_board(board):
     for row in board:
          print(" ".join('Q' if x==1 else '.' for x in row))
     print()


N = int(input("Enter no. of queens: "))
board=[[0 for _ in range(N)] for _ in range(N)]
if solve_queen(board,N,0):
    print_board(board)
else:
     print("Solution does not exist")

