#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dynamically typed language
a=10
b=20
print("sum of a+b=",a+b)


# In[2]:


a=10
type(a)


# In[3]:


a=10.5
type(a)


# In[5]:


a="maresh"
type(a)


# In[6]:


a=True
type(a)


# In[8]:


def f1():
 print("this is maresh")
f1()


# In[11]:


class  test:
 def m1(self):
        print("this is maresh")
t=test()
t.m1()


# In[12]:


# opening text file from laptop
print(open('abc.txt').read())


# In[19]:


#find the address of variable
a=20
print(a)
print(type(a))
id(a)


# In[22]:


#binary numbers
a=111
b=0b111
print(a,b)
print(type(a))
print(type(b))


# In[21]:


#octal number
a=0o123
print(a)


# In[23]:


# hexadecimal number
a=0xab
print(a)


# In[26]:


#number conversions
bin(15)


# In[27]:


bin(0o123)


# In[28]:


bin(0xab)


# In[29]:


oct(123)


# In[30]:


oct(0b111)


# In[31]:


oct(0xab)


# In[32]:


hex(123)


# In[33]:


hex(0b111)


# In[34]:


hex(0o73)


# In[36]:


#complex data type
x=10+20j
print(type(x))
print(x.real)
print(x.imag)


# In[38]:


a=10
b=20
c=a>b
print(c)
print(type(c))


# In[39]:


print(True+True)
print(True+False)
print(False+False)
print(True-False)


# In[40]:


# strings
a="this is maresh"
print(a)
print(type(a))


# In[42]:


print(a[0])
print(a[3])
print(a[-1])


# In[43]:


#slice operator
a="maresh sasha prince sunitha"
print(a)
print(a[:])
print(a[1:])
print(a[:8])


# In[44]:


#converting string to upper case
b=a[0].upper()+a[1:]
print(b)


# In[46]:


b=a[0:len(a)-1]+a[-1].upper()
print(b)


# In[47]:


# adding two strings
a='maresh'+"sunith"
print(a)


# In[49]:


a="maresh"+"10"
print(a)


# In[53]:


a="maresh"*5
print(a)


# In[55]:


a=3*"maresh"
print(a)


# In[ ]:


#type casting

