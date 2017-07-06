
# coding: utf-8

# In[25]:

MEAN_SECONDS = 5 # * 60
STD_SECONDS = 1 # * 60

ACTIONS = [
    'Flip a cup!',
    'Action 2',
    'Action 3',
]


# In[26]:

from random import gauss, choice
import time
from subprocess import call


# In[27]:

def start_flip_cup_timer():
    try: 
        while True:
            interval = gauss(MEAN_SECONDS, STD_SECONDS)
            action = choice(ACTIONS)
            print 'Sleeping for {} seconds'.format(interval)
            time.sleep(interval)
            call(['say', action])
    except KeyboardInterrupt:
        pass


# In[28]:

start_flip_cup_timer()


# In[ ]:



