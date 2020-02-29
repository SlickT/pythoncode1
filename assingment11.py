Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
n=int(input("Enter the average height of ten people: "))
a=[]
for i in range(0,10):
    height=int(input("Enter height: "))
    a.append(height)
avg=sum(a)/n
print("Average height 0f 10 people is",round(avg,2))
