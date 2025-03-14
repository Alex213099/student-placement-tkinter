K=list()
V1=list()
V2=list()
N=eval(input("Enter # of items \n"))

for i in range (N):
    k =input("Enter a key at :"+str(i))
    K.append(k)
    n=input("Enter name at :"+str(i))
    V1.append(n)
    c=input("Enter a key at :"+str(i))
    V2.append(c)

D=dict(zip(k,zip(V1,V2)))
print(D.keys)
print(D.values)
print(D.items())

for k, (v1,v2) in D.items():
    print(f"{k}\l\t{V1}\t\t{V2}\n )
    