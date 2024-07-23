n=int(input("enter number:"))
i=1
while i<=n:
    j=5
    while j>=i:
        print("*" ,end= " ")
        j-=1
    print()
    i+=1