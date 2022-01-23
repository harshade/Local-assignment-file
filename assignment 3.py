#!/usr/bin/env python
# coding: utf-8

# 1.why are functions advantageous to have in your programs?
# 

#  Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update. The main advantage of functions is code Reusability.

# 2. When does the code in a function run: when it's specified or when it's called?

#  The code in a function executes when the function is called function run.it isnot when the function is specified

# 3. What statement creates a function?

# the def statement defines  FUNCTION

# In[7]:


def my(name):
    print("hello"+" " +name)


# In[8]:


my("harsha")


# 4. What is the difference between a function and a function call?

# A function is a block of code that does a particular operation and returns a result. It usually accepts inputs as parameters and returns a result. The parameters are not mandatory.

# while function call is using this function to achive that task. Using a function to do a particular task any point in program is called as function call.

# 5. How many global scopes are there in a Python program? How many local scopes?

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

# # global scope
# X = 99                # X and func assigned in module: global
#           
# def func(Y):          # Y and Z assigned in function: locals
#     # local scope
#     Z = X + Y         # X is not assigned, so it's a global
#     return Z
# 
# func(1)               # func in module: result=100

#  local scope is created whenever a function is called.

# 6. What happens to variables in a local scope when the function call returns?

# When a function returns, the local scope is destroyed, and all the variables in it are forgotten.

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?

# A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

# If a function does not have a return statement, what is the return value of a call to that function?

# its return value is None.

# What is the data type of None?

#  The data type of None is NoneType.

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

# This function can be called with spam.bacon().

# In[27]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')


# In[ ]:


13. What can you do to save a programme from crashing if it encounters an error


# Place the line of code that might cause an error in a try clause and use except block to handle the error.

# 14. What is the purpose of the try clause? What is the purpose of the except clause?

# The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.

# In[ ]:




