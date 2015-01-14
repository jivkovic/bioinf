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