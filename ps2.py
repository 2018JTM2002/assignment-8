###### this is the second .py file ###########

####### write your code here ##########
#rotate function
def rotate(lst,x):
    copy = list(lst)
    for i in range(len(lst)):
        if x<0:
            lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]


#Create 3 groups
a1="abcdefghi"
a2="jklmnopqr"
a3="stuvwxyz_"

b1 =[]
b2 =[]
b3 =[]
i1=[]
i2=[]
i3=[]

#get key vakue from user
k1,k2,k3 = list(map(int,input().split()))

#get string
msg = input()
msg_list = list(msg)
#print(msg_list)

#now compair g1 in string and copy similaar char into s1
for i in range(0,len(msg)):
	if msg_list[i] in a1:
		b1.append(msg_list[i])
		i1.append(i)
		
	elif msg_list[i] in a2:
	    b2.append(msg_list[i])
	    i2.append(i)
	elif msg_list[i] in a3:
	    b3.append(msg_list[i]) 
	    i3.append(i)



#rotate b1,b2,b3
rotate(b1,k1)
rotate(b2,k2)
rotate(b3,k3)



#get decrypted msg
p=q=r=0
for i in range(0,len(msg)+1):
	if i in i1:
		msg_list[i]=b1[p]
		p+=1
	elif i in i2:
		msg_list[i]=b2[q]
		q+=1
	elif i in i3:
		msg_list[i]=b3[r]
		r+=1	

#print(msg_list)

for i in msg_list[:]:
	print (i, end ='')

print("")
