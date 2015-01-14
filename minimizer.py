Genome = "231032101233101"
w = 4
k = 3
l = w+k-1

internal_minimizers = []
end_minimizers = []


def internal(str):
  array = []
  
  for i in range (0, len(str)-k+1):
    array.append(str[i:i+k])
    
  array.sort()
  return array[0]
  
  
def end(str):
  array = []
  
  for i in range (0, len(str)-k+1):
    array.append(str[i:i+k])
    
  array.sort()
  return array[0]
  

for i in range (0, len(Genome)-l+1):
  print internal(Genome[i:i+l])
  
print "\r-\r"
for i in range (0, len(Genome)-k+1):
  print end(Genome[0:i+k])

