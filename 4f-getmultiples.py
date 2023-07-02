def getsumofmultiples (numbers,x): 
    sum=0
    for i in numbers:
        
        if i%x==0:
            sum=sum+i
    if sum==0:
        return -1
    else:
        return sum 
                
numbers=list(map(int,input().split())) 
x=int(input())
print("sum=",getsumofmultiples(numbers,x))
