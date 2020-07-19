class Node():
  def __init__(self):
    self.last=False
    self.child={}
  
  def insert(self,char):
    if char not in self.child:
      self.child[char]=Node()
  
  def suffix(self,suffix=''):
    list1=[]
    for i in self.child:
      if self.child[i].last:
        list1.append(suffix+i)
      list1.extend(self.child[i].suffix(suffix+i))
    return list1

class Trie:
  def __init__(self):
    self.root=Node()
  
  def insert(self,word):
    node=self.root

    for i in list(word):
      if not node.child.get(i):
        node.child[i]=Node()
      node=node.child[i]
    node.last=True
  
  def search(self,key):
    if not key:
      return self.root
    node=self.root
    

    for i in list(key):
      if not node.child.get(i):
        break
      node=node.child[i]
    return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)




ans = MyTrie.search("an")
print(ans.suffix())


ans = MyTrie.search("ant")
print(ans.suffix())



ans = MyTrie.search("f")
print(ans.suffix())


#edge case
ans = MyTrie.search("tripod")
print(ans.suffix())

ans = MyTrie.search("")
print(ans.suffix())




    
      
