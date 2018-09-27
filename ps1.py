###### this is the first .py file ###########

####### write your code here ##########

n=int(input("enter the value of rows n :"))
m=int(input("enter the value of coloumn m:"))
patt = []

#creating a array to take the inputs
for i in range(n):
        t = list(input())
        patt = patt + [t]
print(patt)

#running a loop to compare elements
for i in range(n):
        for j in range(m):
                #print(i,j,patt[i][j])

                if patt[i][j]=='S'and patt[i][j+1]=='S' and patt[i][j-1]=='S': # comparision of characters for finding a pattern of 9 S
                        if patt[i+1][j]=='S'and patt[i+1][j-1]=='D' and patt[i+1][j+1]=='D': #comparision of next column to find the pattern
                                if patt[i+2][j-2]=='S' and patt[i+2][j+2]=='S' and  patt[i+2][j+1]=='S' and patt[i+2][j-1]=='S'and patt[i+2][j]=='S': #comparision in the next row and about the same column against its previous and next column 
                                        if patt[i+3][j]=='S'and patt[i+3][j-1]=='D' and patt[i+3][j+1]=='D':#moving to next row and trying to correlate the pattern 
                                                if patt[i+4][j]=='S'and patt[i+4][j+1]=='S' and patt[i+4][j-1]=='S':   
                                                        print("9")

                elif patt[i][j]=='S' and patt[i][j-1]=='D' and patt[i][j+1]=='D' and i<=n-1 : #similarly trying to correlate the pattern regarding 5 S
                        if patt[i+1][j]=='S' and patt[i+1][j+1]=='S' and patt[i+1][j-1]=='S':
                                if patt[i+2][j]=='S' and patt[i][j-1]=='D'and patt[i][j+1]=='D':
                                                print("5")
                elif patt[i][j]=='S' and patt[i][j-1]=='D' and patt[i][j+1]=='D' and i<=n-1 :# similarly trying tyo correlate the pattern regarding 1 S
                        if patt[i+1][j]=='D'and patt[i+1][j-1]=='D' and patt[i+1][j+1]=='D':
                                if patt[i+2][j]=='D'and patt[i+2][j-1]=='D' and patt[i+2][j+1]=='D':
                                        print("1")



