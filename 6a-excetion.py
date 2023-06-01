class InvalidInputError(Exception):pass
n=int(input("Enter the Mobile Number:"))
count=0
while(n>0):
    count+=1
    n//=10
if(count==10):
    print("Thanks for Entering Valid Mobile number")
else:
    raise InvalidInputError("Enter the Valid Mobile Number!!!")
