#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


x=float(input("Enter the element:"))
mem_young = 1/(1+abs((x-0)/20)**(2 * 2))
mem_old = 1/(1+abs((x-100)/30)**(2 * 3))
print(' 1. More or less young --> {}'.format(np.sqrt(mem_young))) # dialte

print(' 2. Not young and not old --> ', min((1-mem_young),(1-mem_old)))

print(' 3. Young but not too young --> ', min(mem_young,(1-(mem_young)**2)))

print(' 4. Extremely old --> {}'.format((mem_old)**2))


# In[ ]:




