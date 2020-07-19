def get_min_max(ints):
  if not ints:
      return
  maximum=-99999999999999999999
  minimum=99999999999999999999

  for i in ints :
    if(i>maximum):
      maximum=i
    if(i<minimum):
      minimum=i
  
  return (minimum,maximum)

## Example Test Case of Ten Integers
import random

l = [int(i) for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  #pass
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")   #pass
print ("Pass" if (None == get_min_max([])) else "Fail")  #pass