#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Point3D:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point=Point3D(1,2,3)
my_point
    
    
        

  




# In[7]:


class Rectangle:
    
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        return self.length *self.width
    def rectangle_perimeter(self):
        return (self.length+self.width)*2
my_rectangle=Rectangle(3,4)
print(my_rectangle.rectangle_area()) 
print(my_rectangle.rectangle_perimeter())

    


# In[12]:


class Circle:
    
    def __init__(self,r):
        self.radius=r
    def circle_area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
    


    
    


# In[13]:


balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

deposit(5000)
withdraw(100)
deposit(50)
withdraw(4000)


# In[ ]:




