n=int(input("how many students: "))
a=[]
t=[]
p=[]
g=[]
for i in range(n):
    x=input("name: ")
    m1=int(input("marks1: "))
    m2=int(input("marks2: "))
    m3=int(input("marks3: "))
    s=m1+m2+m3
    pr=s/300*100
    if pr>=90:
        gr="A"
    elif pr>=75:
        gr="B"
    elif pr>=60:
        gr="C"
    elif pr>=40:
        gr="D"
    else:
        gr="F"
    a.append(x)
    t.append(s)
    p.append(pr)
    g.append(gr)
for i in range(n):
    print(a[i],t[i],p[i],g[i])
sm=0
for i in range(n):
    sm=sm+p[i]
print("avg",sm/n)
mx=0
for i in range(n):
    if t[i]>mx:
        mx=t[i]
        nm=a[i]
print("topper",nm)
