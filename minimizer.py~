#!/usr/bin/python

import sys, time, resource

# init
inputFile = sys.argv[1]

w = int(sys.argv[2])
k = int(sys.argv[3])
l = w+k-1

minimizers = []
  
    
# function for finding a minimal substring (minimizer) within a substring
def minimizer(str):
  array = []
  
  for i in range (0, len(str)-k+1):
    array.append(str[i:i+k])
    
  array.sort()
  return array[0]

# function for finding left end minimizers
def left_end(str):
  array = []
  
  for i in range (k, l):
    array.append(minimizer(str[0:i]))
    
  return array
  
# function for finding right end minimizers
def right_end(str):
  array = []
  
  for i in range (0, l-k):
    array.append(minimizer(str[i:l]))
    
  return array
  
# function for removing consecutive duplicates and perserve order
def remove_duplicates(array):
  newArray = []
  
  for str in array:
    if (len(newArray) == 0 or newArray[-1] != str):
      newArray.append(str)
      
  return newArray
  
  
  
# main

# start clock
time_start = time.clock()

# file input
with open (inputFile, "r") as myfile:
  Genome=myfile.read().replace('\n', '').replace('\r', '')
  
# find left end minimizers
for str in left_end(Genome[0:l]):
  minimizers.append(str)

# find interior minimizers
for i in range (0, len(Genome)-l+1):
  minimizers.append(minimizer(Genome[i:i+l]))
  
# find right minimizers
for str in right_end(Genome[len(Genome)-l+1:len(Genome)+1]):
  minimizers.append(str)
  
# remove consecutive duplicates
minimizers = remove_duplicates(minimizers)

# save output to file
f = open('output.txt','w')
for item in minimizers:
  f.write("%s\r" % item)
f.close()

# stop clock and profile memory
time_elapsed = (time.clock() - time_start)
memory_used  = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  
# finish
print "Minimizers generated!"
print "Time elapsed: ", time_elapsed, "seconds"
print "Memory used: ",  memory_used,  "KB"