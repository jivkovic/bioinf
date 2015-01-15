#Genome = "231032101233101"
w = 4
k = 3
l = w+k-1

with open ("tests/test10.txt", "r") as myfile:
    Genome=myfile.read().replace('\n', '').replace('\r', '')
    
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
  internal_minimizers.append(internal(Genome[i:i+l]))
  
#remove duplicates
internal_minimizers = list(set(internal_minimizers))

f = open('output.txt','w')
for item in internal_minimizers:
  f.write("%s\n" % item)
f.close()
  
print "\r-\r"
#for i in range (0, len(Genome)-k+1):
#  end_minimizers.append(end(Genome[0:i+k]))
  
print "done!"