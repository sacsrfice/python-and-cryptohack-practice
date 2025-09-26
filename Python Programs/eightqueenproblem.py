N = 8 #board size

#check whether position (n,c) is free from attacks
def isplaceok(a, n, c):
    for i in range(n):    #for each queen already placed
        if (a[i] == c) or (a[i] - i == c - n) or (a[i] + i == c + n):    #same column, diagonal, or diagonal?
            return False    #place can be attacked
    return True    #place is safe

#print a board
def printsolution(a):
    for i in range(N):  #for each row
        for j in range(N):  #for each column
            if a[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print("\n")
    print("\n")

#add to board 'a' all queens from 'n' to 'N'
def addqueen(a, n):
    if n >= N:
        printsolution(a)
    else:
        for c in range(N):  #for each column
            if isplaceok(a, n, c):  #if place is safe
                a[n] = c  #place queen
                addqueen(a, n+1)  #recur to place next queen

#run program
addqueen([-1]*N, 0)
