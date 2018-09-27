###### this is the first .py file ###########

####### write your code here ##########

print("no of rows and no of columns")
n=int(input("value of the row"))
m=int(input("value of the column"))
print(n,m)

lis = []

for i in range(n):
	s=list(input())
	lis+=[s]

print(lis)
 
      
    # initializing value corresponding to 'A'  
    # ASCII value 
 
  
    # outer loop to handle number of rows 
    # 5 in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # explicitely converting to char 
            ch = lis[i:j] 
          
            # printing char value  
            print(ch, end=" ") 
      
        # incrementing number 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 

