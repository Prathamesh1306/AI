def magic_square(n):
   magic_square=[[0]*n for _ in range(n)]
   i=0
   j=n//2

   for num in range(1,n*n+1):
      magic_square[i][j]=num

      newi = (i-1)%n
      newj = (j+1)%n

      if magic_square[newi][newj]:
         i= (i+1) %n   # next row
      else:
         i,j=newi,newj           

   print(f"Magic square of order: {n}")
   for row in magic_square:
      print(row)

n=int(input("Enter the odd no: "))
magic_square(n)
