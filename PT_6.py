
str1='aavvggttrf'
d1={}
for i in str1:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
output_str=' '
for k,v in d1.items():
    output_str=output_str+k+str(v)
print(output_str)

import sys
sys.exit()

str1='accvfgsttsgesfyaa'
d1={}
for i in str1:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)
#o/p--{'a': 3, 'c': 2, 'v': 1, 'f': 2, 'g': 2, 's': 3, 't': 2, 'e': 1, 'y': 1}
import sys
sys.exit()

d1={}

number_data=int(input("how many data you need to insert"))
for i in range(number_data):
    key_from_data=input('enter the key')
    value_from_user=input("enter the values")
    d1[key_from_data]=value_from_user
print(d1)


import sys
sys.exit()

l1=[10,2,3,4,5,60,6,7,8,4]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]==10:
            print(l1[i]+l1[j])
            # l1[i],l1[j]=l1[j],l1[i]

print(l1)


import sys
sys.exit()

str1='a4k3b7c8'
output=''
for i in str1:
    if i.isalpha():
        output=output+i
        prev=i
    else:
        output=output+chr(ord(prev)+int(i))
print(output)

import sys
sys.exit(0)

# reverse the string in even
str1='hi pune good morning'
output='ih pune doog morning'
l1=str1.split()
l2=[]
for i in range(len(l1)):
    if i%2!=0:
        l2.append(l1[i][::-1])
    else:
        l2.append(l1[i])
print(' '.join(l2))

import sys
sys.exit(0)

# reverse the word
str1='hi pune good morning'
output='ih enup doog gninrom'
l1=str1.split()
l2=[]
for i in l1:
    l2.append(i[::-1])
print(' '.join(l2))

import sys
sys.exit(0)
# reverse the string
str1='hi pune good morning'
output='morning good pune hi'
l1=str1.split()
print(' '.join(l1[::-1]))

import sys
sys.exit(0)

# duplicate remove
str1='abcaaabbbcccdefghhh'
output='abcdefgh'
l1=[]

for i in str1:
    if i not in l1:
        l1.append(i)
    else:
        l1.remove(i)
print(l1)


import sys
sys.exit(0)

# find how many number or alphabates use in isalpha
str1='a23b45c1def'
num=''
str2=''
for i in str1:
    if i.isalpha():
        str2=str2+i
    else:
        num=num+i
print(num)
print(str2)

import sys
sys.exit(0)

# find how many number or alphabates use in isdigit
str1='a23b45c1def'
num=''
str2=''
for i in str1:
    if i.isdigit():
        num=num+i
    else:
        str2=str2+i
print(num)
print(str2)
