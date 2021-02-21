#!/usr/bin/env python
# coding: utf-8

# In[15]:


import cv2


# In[16]:


import matplotlib.pyplot as plt


# In[18]:


cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret , frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False
    img100 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img100)
plt.title("image Camera1")
plt.show()
cap.release()


# In[ ]:




