#  *
# *** 
#*****
# *** 
#  *

l=[]
n1=int(input())

for i in range(n1):
    if i==n1//2 + 1:
        for i in range(n1//2):
           print(l[n1//2-i])
        for i in range(n1//2 + 1):
            print(l[i])
        break
    l.append((i*" ")+((n1-i*2)*"*")+(i*" "))

print(l)




        