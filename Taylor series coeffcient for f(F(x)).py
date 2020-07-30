#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[13]:


def partition ( number ):
    answer = set ()
    answer .add (( number , ))
    for x in range (1, number ):
        for y in partition ( number - x):
            answer . add( tuple ( sorted ((x, ) + y )))
    return list ( answer )


# In[14]:


def partition_number ( number ):
    return len( partition ( number ))
def faa_di_bruno_coeff ( order ):
    n = sum( order )
    count = np. zeros (n+1)
    for i in range (n +1):
        count [i] = order . count (i)
    answer = math . factorial (n)
    for i in range (n +1):
        answer = answer /( math . factorial ( count [i]) * math . factorial (i )**( count [i ]))
    return int( answer )


# In[15]:


def taylor_Fx ( derivatives , k):
    answer = var('q')
    for i in range (k):
        answer = answer + var('x')**( i +1)* derivatives [i ]/( math . factorial (i +1))
    return answer


# In[16]:


def taylor_Fxoverf1 ( derivatives , k):
    answer = var('q')
    for i in range (k):
        answer = answer + var('x')**( i +1)* derivatives [i ]/( math . factorial (i +1)* f1 **(i +1))
    return answer


# In[17]:


def fx(x,d):
    return 1-(1-x**d )**d


# In[20]:


d = 6
derivatives_F = [var('f1 ')* var('F1 ')]
derivatives_F_0 = [1]
for i in range (2,d):
    terms = 0
    orders = partition (i)
    for order in orders :
        if len( order ) is not 1:
            term = 1
            term = term * var('f'+ str( len( order )))
            for power in order :
                # term = term * var('F '+str( power ))
                term = term * derivatives_F_0 [power -1]
            term = term * faa_di_bruno_coeff ( order )
            terms = terms + term
terms = terms / (var('f1 ')**i-var('f1 '))
derivatives_F_0 . append ( terms )


# In[ ]:




