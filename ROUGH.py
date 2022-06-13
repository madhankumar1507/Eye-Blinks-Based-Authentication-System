'''k=int(input())
n=0
l=1
if k==2:
    print(n)
    print(l)
elif k==1:
    print(n)
else:
    print(n)
    print(l)
    for i in range(3,k+1):
        m=n+l
        n=l
        l=m
        print(m)'''






#SELECT ID,NAME FROM CUSTOMER WHERE COUNTRY='USA' AND CREDITS>100000;






'''n=int(input())
lst1=[]
for i in range(n):
    lst1.append(int(input()))
m=int(input())
lst2=[]
for i in range(m):
    lst2.append(int(input()))
count=0
k=lst1+lst2
k.sort()
j=[]
for i in range(len(k)):
    if k[i] in lst1:
        j.append(0)
    else:
        j.append(1)
for i in range(len(j)-1):
    if j[i]!=j[i+1]:
        count+=1
print(count)'''



'''s=list(palindromeStr)
c=0
for j in range(len(s)-1):

    for i in range(j+1,len(s)):
        if ord(s[j])>ord(s[i]):
            s[j]=s[i]
            c+=1
            break
    if c==1:
        break
if m!= "".join(s):
    print("".join(s))
else:
    print("IMPOSSIBLE")'''













#SELECT ID FROM COMPANY WHERE EMPLOYEES>10000;






#SELECT ;
























'''s=int(input())
m="Y"*s
print(m)
n=['YYY','YYY','YNN','YYY','YYY','YYY','YYY','YNY','YYY','YYY','YYY','YYY','YYY','YYY','YYY']
l=[]
c=0
for i in range(len(n)):
    print(i)
    if n[i]==m:
        print(i)
        c+=1
    else:
        l.append(c)
        c=0
    if i==len(n)-1:
        l.append(c)
print(l)
k=max(l)
print(k)'''











'''l=[22,121]
c=0
for i in range(len(l)):
    for j in range(int(l[i])):
        if j+int(str(j)[::-1])==int(l[i]):
            c+=1
            break
print(c)'''


'''if($4>=25){
    if($3=="Comedy"){
       if($2=="Telugu"){
count=count+1
}

}
}
    END{
    if(count>0){
    print c
}
else{
    print "No records found"
}
}'''




'''input1=input()
input2=input()

m="".join(sorted(input1))
n="".join(sorted(input2))
if m==n:
    print("yes")
else:
    print("no")'''









#121
'''
#using permutations for making some combos 
from itertools import permutations
#taking inputs
string=input()
k=int(input())
#initializing count
count=0
#making a list for permutations
set_list=list(range(0,len(string)))
combo_list=list(permutations(set_list,k))
for i in range(len(combo_list)):
    combo=combo_list[i]
    dup_str=list(string)
    for j in range(len(combo)):
        dup_str[combo[j]]=''
    fin_str=''
    for j in range(len(dup_str)):
        if dup_str[j]!="":
           fin_str+=dup_str[j]

    if fin_str==fin_str[::-1]:
        print(fin_str)
        count+=1
        break
if count>0:
    print("YES")
else:
    print("NO")'''
#123
'''n=input()
if n.isnumeric() or n[1:].isdigit():
    print("YES")
elif '.' in n:
    k=n.index('.')
    if n[k+1:].isdigit():
        print("YES")
elif 'e' in n:
    k=n.index('e')
    if n[:k].isnumeric() and n[k+1:].isdigit():
        print("YES")
else:
    print("NO")'''
#124
'''n=int(input())
def flips(n):
    count=0
    while n!=1:
        count+=1
        n=n//2
    return count
print(flips(n))'''
#126
'''list=list(map(int,input().split()))
n=int(input())
def rotations(list,n):
    count=0
    for i in range(n):
        k = list[0]
        for j in range(len(list)):
            if j!=len(list)-1:
                list[j]=list[j+1]
                count+=1
            else:
                list[j]=k
                count+=1
    list.append(count)

    return list
fin_list=rotations(list,n)
print("Final list is",fin_list[0:len(fin_list)-1])
print("no.of swaps required is :",fin_list[-1])'''
















'''n=int(input())
s=input()
b=int(input())
g=int(input())
def fillSeats(n,s,B,G):
    b=B
    g=G
    c=0
    s=list(s)
    for i in range(len(s)):
        if s[i]=='0' and g>0:
            print(i)
            if i!=len(s)-1:
                if s[i+1]!="g" and s[i-1]!="g":
                    g-=1
                    s[i]='g'
                    c+=1
            else:
                if s[i - 1] != "g":
                    g-=1
                    s[i]='g'
                    c+=1
        if s[i]=='0' and b>0:
            print(i)
            if i!=len(s)-1:
                if s[i+1]!="b" and s[i-1]!="b":
                    g-=1
                    s[i]='b'
                    c+=1
            else:
                if s[i - 1] != "b":
                    g-=1
                    s[i]='b'
                    c+=1
    
    return c'''













'''from itertools import combinations













n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
    
    
    
    
    
    
    
    
lst=list(range(0,len(l)))
k=list(combinations(lst,2))
fin=[]
for i in range(len(k)):
    d=l
    m=list(k[i])
    h=m[0]
    g=m[1]
    o=d[h]&d[g]
    a=d[h]|d[g]
    d[h]=o
    d[g]=a
    c=0
    for j in range(len(d)):
        c+=d[j]**2
    fin.append(c)
return(max(fin))'''



'''N=int(input())
K=int(input())
l=[]
for i in range(N):
    l.append(int(input()))

lst=[]
l.sort()
for i in range(len(l)-1,-1,-1):
    if l[i]%2==0:
        lst.append(l[i])
        if len(lst)==K:
            break
c=0
k=[]
for i in range(len(lst)):
    if (lst[i]//2)%2==0:
        k.append(lst[i]//2)
        c+=1
    else:
        for j in range(lst[i]//2):

            k.append(2)
            c+=1
    lst=k
    k=[]
print(len(lst)+c)'''




'''n=int(input())
l=list(map(int,input().split()))
l.sort()
print(l[-2]*l[-3])'''






c=0
for i in range(0,7<<2):
    c+=2

print(c)








































