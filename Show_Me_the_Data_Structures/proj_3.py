import sys
import heapq as heap

huffdecoding={}
huffcoding={}


class Node: 
  def __init__(self,key,value):
    self.key=key
    self.value=value 
    self.left = None
    self.right = None
  def __lt__(self, v):
    return self.value<v.value

def preorder(root,string):
  global huffdecoding
  if(root.right==None and root.left==None):
    huffdecoding[string]=root.key 
    huffcoding[root.key] =string
    return 
  preorder(root.left,string+'0')
  preorder(root.right,string+'1') 

def frequency(data):
  map_frequency={}
  for i in data:
    if i in map_frequency:
      map_frequency[i]+=1
    else:
      map_frequency[i]=1
  return map_frequency

def huffman_encoding(data):
  map_frequency=frequency(data)
  global huffdecoding
  global huffcoding
  huffdecoding.clear()
  huffcoding.clear()

  map_frequency={}
  for i in data:
    if i in map_frequency:
      map_frequency[i]+=1
    else:
      map_frequency[i]=1
  
  nodesmap=[]
  for key,value in map_frequency.items():
    p=Node(key,value)
    heap.heappush(nodesmap,p)

  heap.heapify(nodesmap)
  length=len(nodesmap)
  
  for i in range(length-1):
    elements=heap.nsmallest(2,nodesmap)
    a=heap.heappop(nodesmap)
    b=heap.heappop(nodesmap)
    roots=Node(None,a.value+b.value)
    roots.left=a
    roots.right=b
    heap.heappush(nodesmap,roots)
  
  strings=""
  r=roots
  decoded_string=""
  preorder(r,strings) 
  
  
  for d in data:
    decoded_string+=huffcoding[d]
  return decoded_string

def huffman_decoding(data):
  
  global huffdecoding

  temp=""
  result=""
  for i in data:
    temp+=i
    if temp in huffdecoding:
      result+=huffdecoding[temp]
      temp=""
  return result

def test_Huffman(a_great_sentence):

    codes = {}
    

    #a_great_sentence = ("")
    if a_great_sentence == None:
      print("***************************************************************")
      print(None)
      return
      
    elif a_great_sentence == "":
      print("***************************************************************")
      print("Empty String")
      return
    elif len(frequency(a_great_sentence)) == 1:
      print("***************************************************************")
      code = "0"*len(a_great_sentence)
      print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
      print ("The content of the data is: {}\n".format(a_great_sentence))
      print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
      print ("The content of the encoded data is: {}\n".format(code))
      print ("The size of the decoded data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    else:

      print("***************************************************************")
      print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
      print ("The content of the data is: {}\n".format(a_great_sentence))

      encoded_data = huffman_encoding(a_great_sentence)

      print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
      print ("The content of the encoded data is: {}\n".format(encoded_data))

      decoded_data = huffman_decoding(encoded_data)

      print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
      print ("The content of the encoded data is: {}\n".format(decoded_data))







#normal case:
test_Huffman("udacity")
test_Huffman("huffman")
test_Huffman("mississipi")

#edge case:
test_Huffman(None)
test_Huffman("")
test_Huffman("a")
test_Huffman("aa")