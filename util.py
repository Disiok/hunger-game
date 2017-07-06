from subprocess import call
import time
from random import choice

PLAYERS = [
    'Simon',
    'Rahul',
    'Peng Fei',
    'Mary',
    'Bryan',
    'Ulysses',
]

def print_and_say(sentence, voices=False):
    print sentence
    if voices:
        voice = choice(voices)
        call(['say', '-v', voice, sentence])
    else:
        call(['say', sentence])

def get_available_voices():
    with open('voice_list.txt') as f:
        lines = f.readlines()
        voices = map(lambda x: x.split()[0], lines)
        return voices