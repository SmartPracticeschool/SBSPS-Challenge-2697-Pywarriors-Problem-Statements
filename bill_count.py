'''

x=int(input("Enter the amount:"))
y=input("Enter the list:")
bill_count(x,y)
    

def bill_count(a,e):
    b=list(map(int,e.split()))
    if a<0:
        print("Amount of money should not be negative")
        return
    if min(b)>a:
        print("Amount of money should be greater than or equal to money bills")
        return
    
    f=[1,2,5,10,20,50,100,200,2000]
    for i in b:
        if i not in f:
            print("Enter only Indian currency bills")
            return
        d=0

    while True:
        c=max(b)
        while a%c!=0:
            d=d+a//c
            a=a%c
            b.remove(max(b))
            c=max(b)
        if a%c==0:
           d=d+a//c
           print(d)
           break


