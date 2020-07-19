def sqrt(n):
  if(n<0):
    return -1
  if(n==0 or n==1):
    return n
  start=0
  end=n
  while(start<=end):
    mid=(start+end)//2
    if(mid*mid==n):
      return mid
    elif(mid*mid<n):
      start=mid+1
      ans=mid
    else:
      end=mid-1
  return ans



print ("Pass" if  (3 == sqrt(9)) else "Fail")

print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")

#edge case
print ("Pass" if  (3079932 == sqrt(9485982847545)) else "Fail")
print ("Pass" if  (-1 == sqrt(-27)) else "Fail")