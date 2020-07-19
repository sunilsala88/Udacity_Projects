def fuse(left, right):
    ans = []
    lefts = 0
    rights = 0

    while lefts < len(left) and rights < len(right):

        if left[lefts] < right[rights]:
            ans.append(right[rights])
            rights += 1

        else:
            ans.append(left[lefts])
            lefts += 1


    ans += left[lefts:]
    ans += right[rights:]

    return ans

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]


    left = mergesort(left)
    right = mergesort(right)


    return fuse(left, right)


def rearrange_digits(input_list):
    if len(input_list) <= 1:
        return []

    sorted_list = mergesort(input_list)

    first = sorted_list[0::2]
    second = sorted_list[1::2]
    
    first_string = ''
    for i in first:
        first_string += str(i)

    second_string = ''
    for i in second:
        second_string += str(i)

    return [int(first_string), int(second_string)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])  #pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)                     #pass [edge case]
test_function([[1,1,1,1,1], [111, 11]])      #pass
test_function([[0], [-1, -1]])               #fail
test_function([[0, 0], [0, 0]])             #pass  [edge case]
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])   #pass
test_function([[2, 5], [5,2]]) #pass   
test_function([[],[]]) #  pass
test_function([[1],[]]) # pass 