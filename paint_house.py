costs = [[17,2,3,17],[16,2,16,5],[14,3,19,1]]
p,sum = -100, 0
for line in costs:
  p = line.index(min(line[:p]+line[p+1:]))
  sum += line[p]
print(sum)

#p=-100
#print([line.index(min(line[:p]+line[p+1:])) for line in costs])
  
