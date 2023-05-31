
#!-------------------------------------------------------------------------------------------------------------------------------------
#%                                                     Number Pattern
#!-------------------------------------------------------------------------------------------------------------------------------------
## Example-1
#%  1 1 1 1 1
#%  2 2 2 2
#%  3 3 3
#%  4 4
#%  5
'''
n = int(input("Enter n Value: "))
dummy=1
num=n
for i in range(n):
    for j in range(num):
        print(dummy,end=' ')
    dummy+=1
    num-=1
    print()
'''





## Example-2

#%  1 1 1 1 1
#%    2 2 2 2
#%      3 3 3
#%        4 4
#%          5
'''
n = int(input("Enter n Value: "))
dummy=1
num=n
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
    dummy+=1
    num-=1
    sp+=1
    print()
'''





## Example-3

#%  1
#%  2 2
#%  3 3 3
#%  4 4 4 4
#%  5 5 5 5 5
'''
n = int(input("Enter n Value: "))
dummy=1
num=1
for i in range(n):
    for j in range(num):
        print(dummy,end=' ')
    dummy+=1
    num+=1
    print()
'''






## Example-4

#%          1
#%        2 2
#%      3 3 3
#%    4 4 4 4
#%  5 5 5 5 5
'''
n = int(input("Enter n Value: "))
dummy=1
num=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
    dummy+=1
    num+=1
    sp-=1
    print()
'''






## Example-5

#%  1 2 3 4 5
#%  6 7 8 9
#%  10 11 12
#%  13 14
#%  15
'''
n = int(input("Enter n Value: "))
dummy=1
num=n
for i in range(n):
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num-=1
    print()
'''






## Example-6

#%  1 2 3 4 5
#%    6 7 8 9
#%      10 11 12
#%        13 14
#%          15
'''
n = int(input("Enter n Value: "))
dummy=1
num=n
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num-=1
    sp+=1
    print()
'''





## Example-7

#%  1
#%  2 3
#%  4 5 6
#%  7 8 9 10
#%  11 12 13 14 15
'''
n = int(input("Enter n Value: "))
dummy=1
num=1
for i in range(n):
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num+=1
    print()
'''






## Example-8

#%          1
#%        2 3
#%      4 5 6
#%    7 8 9 10
#%  11 12 13 14 15
'''
n = int(input("Enter n Value: "))
dummy=1
num=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num+=1
    sp-=1
    print()
'''







## Example-9

#%  1 2 3 4 5
#%  1 2 3 4
#%  1 2 3
#%  1 2
#%  1
'''
n = int(input("Enter n Value: "))
num=n
for i in range(n):
    dummy=1
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num-=1
    print()
'''







## Example-10

#%  1 2 3 4 5
#%    1 2 3 4
#%      1 2 3
#%        1 2
#%          1
'''
n = int(input("Enter n Value: "))
num=n
sp=0
for i in range(n):
    dummy=1
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num-=1
    sp+=1
    print()
'''






## Example-11

#%          1
#%        1 2
#%      1 2 3
#%    1 2 3 4
#%  1 2 3 4 5
'''
n = int(input("Enter n Value: "))
num=1
sp=n-1
for i in range(n):
    dummy=1
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(dummy,end=' ')
        dummy+=1
    num+=1
    sp-=1
    print()
'''





## Example-12

#%  1
#%  2 1
#%  3 2 1
#%  4 3 2 1
#%  5 4 3 2 1
'''
n=int(input("Enter n value: "))
dummy=1
for i in range(n):
    num=i+1
    for j in range(dummy):
        print(num,end=' ')
        num-=1
    dummy+=1
    print()
'''





## Example-13

#%          1
#%        2 1
#%      3 2 1
#%    4 3 2 1
#%  5 4 3 2 1
'''
n=int(input("Enter n value: "))
dummy=1
sp=n-1
for i in range(n):
    num=i+1
    for s in range(sp):
        print(' ',end=' ')
    for j in range(dummy):
        print(num,end=' ')
        num-=1
    dummy+=1
    sp-=1
    print()
'''




## Example-14

#%                1 
#%              2 1 2 
#%            3 2 1 2 3 
#%          4 3 2 1 2 3 4 
#%        5 4 3 2 1 2 3 4 5 
#%          4 3 2 1 2 3 4 
#%            3 2 1 2 3 
#%              2 1 2 
#%                1 

'''
n = int(input("Enter n value: "))
sp=n-1
stars=1
for i in range(n):
    num=stars//2+1
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print(num,end=' ')
        if j<stars//2:
            num-=1
        else:
            num+=1
    if i<n//2:
        sp-=1
        stars+=2
    else:
        sp+=1
        stars-=2
    print()
'''



## Example-15
#%   2 
#%     5 
#%       11 
#%         17 
#%           23 
#%         19 
#%       13 
#%     7 
#%   3 
'''
numm=9
n=2
count=0
x=[]
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        count+=1
        x+=[n]
    if count==9:
        break
    n+=1
print(x)
o=[]
e=[]
c=0
for i in x:
    c+=1
    if c%2==0:
        o+=[i]
    else:
        e+=[i]
print(o)
print(e)
new=e+o[::-1]
print(new)
sp=0
st=1
for i in range(numm):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(st):
        print(new[i],end=' ')
    if i<numm//2:
        sp+=1
    else:
        sp-=1
    print()
'''





## Example-16

#%  1
#%    3
#%      5
#%        7
#%          9
#%        8
#%      6
#%    4
#%  2
'''
numm=9
o=[]
e=[]
count=0
for i in range(1,numm+1):
    count+=1
    if count%2==0:
        o+=[i]
    else:
        e+=[i]
print(o)
print(e)
l=e+o[::-1]
print(l)
sp=0
st=1
for i in range(numm):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(st):
        print(l[i],end=' ')
    if i<numm//2:
        sp+=1
    else:
        sp-=1
    print()
'''




## Example-17
#%  1
#%    3
#%      8
#%        21
#%      13
#%    5
#%  2


numm=7
x=[]
f=0
s=1
for i in range(numm):
    t=f+s
    f,s=s,t
    x+=[t]
print(x)
e=[]
o=[]
count=0
for j in x:
    count+=1
    if count%2==0:
        o+=[j]
    else:
        e+=[j]
print(e)
print(o)
new=e+o[::-1]
print(new)
sp=0
st=1
for i in range(numm):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(st):
        print(new[i],end=' ')
    if i<numm//2:
        sp+=1
    else:
        sp-=1
    print()