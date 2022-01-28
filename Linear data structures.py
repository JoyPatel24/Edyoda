#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Write a program to find all pairs of an integer array whose sum is equal to a given number?
'''
def getPairsCount(arr, n, sum):
 
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count


# In[2]:


'''
Write a program to reverse an array in place? In place means you cannot create a new array. 
You have to update the original array.
'''
def reverseList(A):
    print( A[::-1])
     


# In[3]:


'''
Write a program to check if two strings are a rotation of each other?
'''
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp=string1+string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0


# In[4]:


'''
Write a program to print the first non-repeated character from a string?
'''
NO_OF_CHARS = 256
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
    return index


# In[5]:


'''
Read about the Tower of Hanoi algorithm. Write a program to implement it.
'''
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)


# In[6]:


'''
 Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
 '''
def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
def postToPre(post_exp):
 
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans


# In[8]:


'''
Write a program to convert prefix expression to infix expression.
'''
def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 


# In[9]:


'''
Write a program to check if all the brackets are closed in a given code snippet.
'''
def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True


# In[10]:


'''
Write a program to reverse a stack.
'''
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
def createStack():
    stack = []
    return stack
def isEmpty( stack ):
    return len(stack) == 0
def push( stack, item ):
    stack.append( item )
def pop( stack ):
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()


# In[11]:


'''
Write a program to find the smallest number using a stack.
'''
from collections import deque
 
class MinStack:
    def __init__(self):
        
        self.s = deque()
     
        self.min = None
 
    def push(self, val):
        if not self.s:
            self.s.append(val)
            self.min = val
        elif val > self.min:
            self.s.append(val)
        else:
            self.s.append(2*val - self.min)
            self.min = val
 
    def pop(self):
        if not self.s:
            self.print('Stack underflow!!')
            exit(-1)
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()
 
    def getMin(self):
        return self.min


# In[ ]:




