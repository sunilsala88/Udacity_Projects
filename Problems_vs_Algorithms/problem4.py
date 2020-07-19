

def sort_012(input_list):
   if(len(input_list)==0):
      return -1

   start=0
   end=len(input_list)-1
   mid=start
   while(mid<=end):
      if(input_list[mid]!=0 and input_list[mid]!=1 and input_list[mid]!=2):
        return -1
        break
        
      if(input_list[mid]==2):
       input_list[mid]=input_list[end]
       input_list[end]=2
       
       
       end-=1

      if(input_list[mid]==0):
        input_list[mid]=input_list[start]
        input_list[start]=0
        mid+=1
        start+=1

      if(input_list[mid]==1):
        mid+=1
   return input_list



    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#edge case
test_function([])
test_function([0, 0, 0, 0, 0, 0, 8, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

