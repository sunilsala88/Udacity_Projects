

def rotated_array_search(input, num):

  start=0
  end=len(input)-1
  while(start<=end):
    mid=(start+end)//2
    if(num==input[mid]):
      return mid
    if(input[start]<input[mid]):
      if(num<input[mid] and num>=input[start]):
        end=mid-1
      else:
        start=mid+1
    else:
      if(num<=input[end] and num>input[mid]):
        start=mid+1
      else:
        end=mid-1
  return -1

  
  
  

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

