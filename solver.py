# John Conor Kenny
# G00301273
# Countdown Solver

# Opens dictionary file.
# Wordlist from http://www.mieliestronk.com/wordlist.html
with open('wordlist.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Takes input from console to use as the anagram.
# This is only really for testing.
testInput = input('Enter word to find: ')

# Running time for the algorithm.
# It starts here, otherwise it takes into account waiting for user input.
import time
start_time = time.time()

# The permutations script will generate every possible combo of a word.
# This does not currently match the countdown rule however.
# If you enter a 9 letter word, it will only return the 9 letter anagrams.
# But it's mad fast and this whole thing is 9 lines including the timing function
from itertools import permutations
perms = [''.join(p) for p in permutations(testInput)]

# Returns where the permutations match the dictionary files.
# Using sets here to remove any duplicates.
print(set(words) & set(perms))

# Prints running time of the script.
print("--- %s seconds ---" % (time.time() - start_time))
