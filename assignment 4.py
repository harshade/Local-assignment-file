#!/usr/bin/env python
# coding: utf-8

# 1.What exactly is [ ]?

# the empty list reprented by []

# 2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[2]:


spam = [2,4,6,8,10]
spam[4] = "hello"
print(spam)


# # Let's pretend the spam includes the list ['a','b','c',d'] for the next three queries.

# 3. What is the value of spam[int(int('3'*2)//11)] ?

# In[8]:


spam=['a','b','c','d']
print(spam[int(int('3'*2)//11)])


# What is the value of spam[-1]?

# In[11]:


spam


# In[12]:


print(spam[-1])


# 5. What is the value of spam[:2]?

# In[13]:


print(spam[:2])


# # Let's pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three question

# # 6. What is the value of bacon.index('cat')?

# In[26]:


bacon=[3.14,'cat',11,'cat',True]
print(bacon.index('cat'))


# 7. How does bacon.append(99) change the look of the list value in bacon?

# In[27]:


bacon


# In[28]:


bacon.append(99)
print(bacon)


# 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[30]:


bacon.remove("cat")
print(bacon)


# 9.what are the list concatenation and list replication operations?

# In[32]:


list1 = ["ha","na","ra"]
list2 = ["ds","ms","sp"]
print(list1 + list2)
print(list2*2)


# 10.what is the difference between the list method append() and insert()?

# While append() will add values only to the end of a list, insert() can add them anywhere in the list.

# In[34]:


list = [1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'trail')
print(list)


# 11. What are the two methods for removing items from a list?

# del and remove()ato remove the valuesre the two methods

# 12. Describe how list values and string values are identical.

# both lists and strings can be passed to len() function, have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

# 13. What's the difference between tuples and lists?
# 

# Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed. Tuples are Immutable but Indexable and Slicable. the tuple values cannot be changed at all. Also, tuples are represented using parentheses, (), while lists use the square brackets, [].

# 14. How do you type a tuple value that only contains the integer 42?

# In[36]:


t1 = (42)
t2 = (42,)
print(type(t1))
print(type(t2))


# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa

# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

# it contain references to list values.

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

# In[ ]:




