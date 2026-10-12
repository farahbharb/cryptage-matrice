from numpy import array
def taillematrice(ch):
    n=1
    while n*n<len(ch):
        n=n+2
    return n
def remplir(ch,m,n):
    k=0
    for i in range(n):
        for j in range(n):
            if k<=len(ch)-1:
                m[i,j]=ch[k]
                k=k+1
            else:
                m[i,j]="*"
def chiffrer(m,n):
    ch=m[round(n/2),round(n/2)]
    k=1
    c=0
    while k<=n/2:
        i=(round(n/2))-k
        j=(round(n/2))-k
        c=c+2
        ch=ch+m[i,j]
        i1=i
        j1=j
        while i1<i+c:
            ch=ch+m[j1,i1+1]
            i1=i1+1
        while j1<j+c:
            ch=ch+m[j1+1,i1]
            j1=j1+1
        while i1>i:
            ch=ch+m[j1,i1-1]
            i1=i1-1
        ch=ch[:len(ch)-1]
        while j1>j:
            ch=ch+m[j1-1,i1]
            j1=j1-1
        ch=ch[:len(ch)-1]
        k=k+1
    return ch
ch="CRYPTAGEPARMATRICE"
n=taillematrice(ch)
m=array([[str]*n]*n)           
remplir(ch,m,n)
ch1=chiffrer(m,n)
print(m)
print(ch1)








