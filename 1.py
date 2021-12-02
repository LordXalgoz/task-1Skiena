print("Введите i и j: ")
i,j = map(int, input().split())
n = j
maxk = 0
for x in range(i,j+1):
    k=1
    n=x
    while n>1:
        k+=1
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
    maxk=max(maxk, k)
    print(x,maxk)
print(i," ",j," ",maxk)
