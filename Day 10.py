n=int(input())
c=0
a=1 
b=2
if(n==0 or n==1):
    print("1")
    
elif(n==2):
    print("2")
else:
   for i in range(3,n+1): 
    c=a+b 
    a=b
    b=c 
print(c)
