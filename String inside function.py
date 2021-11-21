#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Write a Python program to reverse a string.



Sample String : "1234abcd"

Expected Output : "dcba4321"
'''
def string_rev(stri):

    rstri = ''
    index = len(stri)
    while index > 0:
        rstri += stri[ index - 1 ]
        index = index - 1
    return rstri
print(string_rev('1234abcd'))


# In[ ]:




