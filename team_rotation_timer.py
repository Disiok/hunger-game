
# coding: utf-8

# In[78]:

ROUND_TIME = 1
COUNT_DOWN_TIME = 6

ROUND_BEGIN_GREETING = 'Round beginning in'
COUNT_DOWN = ''.join(map(lambda x: '{}, '.format(x), reversed(range(1, COUNT_DOWN_TIME))))
START = 'Start!'
END = 'Game over!'


# In[79]:

from subprocess import call
import time
from random import choice
from utils import *

# In[92]:

def start_rotation_game():
    voices = get_available_voices()
    
    try:
        # greeting
        print_and_say(ROUND_BEGIN_GREETING)
        print_and_say(COUNT_DOWN)
        print_and_say(START)

        while True:
            print 'Sleeping for {} seconds'.format(ROUND_TIME)
            time.sleep(ROUND_TIME)
            print_and_say('Rotate!', voices=voices)
    except KeyboardInterrupt:
        # end
        print_and_say(END)


# In[94]:

start_rotation_game()


# In[ ]:



