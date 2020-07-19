
import hashlib
import datetime 
utc = datetime.datetime.utcnow()

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:
    def __init__(self, data, previous):
      
      self.timestamp = datetime.datetime.utcnow()
      self.data = data
      if previous:
        self.previous_hash = previous.hash
      else:
          self.previous_hash=0
      self.previous_block = previous
      self.hash = calc_hash(str(data))

    def __repr__(self):
        the_block = ("\nBlock Attributes:" +
                     "\n   timestamp: " + str(self.timestamp) +
                     "\n   data: " + str(self.data) +
                     "\n   previous hash: " + str(self.previous_hash) +
                     "\n   hash: " + str(self.hash))
        return the_block

class BlockChain:

    def __init__(self):
        self.root = None
        self.tail=None
        self.size=0


    def append(self, block):
        if self.root is None:
          self.head = block
          self.tail=block
          self.size+=1
          return
        new = block
        new.previous_block = self.tail
        #new.previous_hash=self.tail.hash
        
        self.tail=new
        self.size+=1

    def printchain(self):
      
      block = self.tail
      while block:
        print(block)
        
        block = block.previous_block
      


#Testing code
"""
Case 1
"""
print("TCase 1 ")
a=Block("block 0 data",0)
A = BlockChain()
A.append(a)

print("size",A.size)
A.printchain()
print()


"""
Test Case 2
"""
print("Test Case 2 ")
B = BlockChain()
m=Block("block 1 data",0)
B.append(m)
n=Block("block 2 data",m)
B.append(n)
print("size",B.size)
B.printchain()
print()


"""
 Case 3 multiple chain
"""
print("Test Case 4 Five item BlockChain")
D = BlockChain()
D.append(Block("block 1 data",D.tail))
D.append(Block("block 2 data",D.tail))
D.append(Block("block 3 data",D.tail))
D.append(Block("block 4 data",D.tail))
D.append(Block("block 5 data",D.tail))

print("size",D.size)
D.printchain()

"""
Case 4 
"""
print("edge case")
a=Block("",0)
A = BlockChain()
A.append(a)

print("size",A.size)
A.printchain()
print()
