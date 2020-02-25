#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Input tVo x & y")
x,y = map(int,input().split())
print("TVo x & y are:", x,y)


# In[2]:


from timeit import default_timer
def timer(n):
    start = default_timer()
    #pass
    for row in range(0,n):
        print(row)
    print(default_timer() - start)
    
    


# In[3]:


timer(5)


# In[4]:


timer(13)


# In[5]:


import os.path


# In[6]:


print(os.path.expanduser('~'))


# In[1]:


print('Input tVo x&y')
x,y = map(int,input().split())
print('TVo x&y are: ', x,y)


# In[2]:


from timeit import default_timer
def timer(n):
    start = default_timer()
    #pass
    for row in range(0,n):
        print(row)
    print(default_timer() -start)


# In[3]:


timer(6)


# In[4]:


var_list = ['a','b','c','d']
x,y,z,f = (var_list +[None] * 4)[:4]
print(x,y,z,f)
var_list = [211, 31,36]
x,y = (var_list + [None] * 2)[:2]
print(x,y)


# In[5]:


import json


# In[6]:


print(json.dumps({'Olegsmm2092':1, 'Genrih':2, 'Cicevatov':3}))


# In[7]:


str1 = '233,33'
print('Original String: ', str1)
str1 = str1.ljust(8,'0') # excel кнопка сколько сократить увеличить цифр после точки . 
                        #ljust(на сколько увеличить уменьшить, '0' print контроль
                        #здесь дефка формула подсчитанных значений)
print(str1)
str1 = str1.ljust(11,'0')
print(str1)


# In[10]:


str1 = 'B9349j934bdfgPVFJ'
print(any(d.islower() for d in str1))


# In[11]:


from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))


# In[16]:


x = 31
y = 31
z = 32
if x == y == z == 31:
    print('All variables have same value')
else:
    print('Not all variables have some value')
    print('All variables havent same value')


# In[17]:


import collections
num = [3,3,5,7,9,7,13,5]
print(sum(collections.Counter(num).values())) # excel формула =сум  sum( .Counter(параметр).values())


# In[18]:


words = ['a','b','c','d']
print(sum(collections.Counter(words).values()))


# In[19]:


import sys
print('Float value info: ', sys.float_info)
print('\nInteger vi: ',sys.int_info)
print('\nMax size oa integer: ',sys.maxsize)


# In[20]:


n = 31
d = {'x':513}
l = [2,4,6]
t = (6,8,9)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())


# In[22]:


try:
    x = 1
except NameError: # не работает google yb как использовать except 
    print('Variable isnt defined ....')
else:
    print('Variable is defined')
try:
    y
except NameError:
    print('Variable isnt defined....')
else:
    print('Variable is defined')
    


# In[24]:


str_num = '234567890'
print()
print('%.5s' % str_num) #тонкости кол-во цифр из переменной напечатать
print()


# In[27]:


str_words = 'x,y,z,f'
print()
print('%.3s' % str_words)
print()


# In[28]:


order_amt = 323.485
print('\nT total order amount comes to %f' % order_amt)
print('\nT total order amount comes to %.2f' % order_amt) # excel кнопка после запятой
                                                 #print(' %.numf' % переменная)
print()


# In[31]:


print()
nums = [21, 31,67,36,28,113]
values = bytearray(nums)
for d in values: print(d) # excel кнопка перевернуть x on the y 
print()


# In[32]:


str1 = 'Olegsmm2092'
str2 = 'Olegsmm2092'

print('\nMemory location of str1 =', hex(id(str1)))
print('\nMemory location of str2 =', hex(id(str2)))
print()


# In[33]:


str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'

print(str)


# In[36]:


from functools import reduce
nums = [21,31,41]
nums_product = reduce((lambda x,y: x*y), nums)
print('Product ot nums: \n',nums_product)


# In[ ]:




