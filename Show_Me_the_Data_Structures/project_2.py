
import os
answer=[]

def find_files(suffix, path):
  if suffix == '':  # No proper suffix input
        return []


  if len(os.listdir(path)) == 0:  # Stopping condition
        return []
 

  temp = suffix
  global answer  
  if path:
      temp = suffix + '/' + path
  
  for f in os.listdir(temp):
    
    filepath = temp +  '/' + f

    if os.path.isfile(filepath) and filepath.endswith(".c"):
      answer.append(filepath)
    elif os.path.isdir(filepath):
       answer = find_files(temp, f)

  return answer

print(find_files('.', 'testdir'),end='\n ')
print(find_files('.', 'testdir/subdir5'),end='\n')

# Edge Cases:
print(find_files('', 'testdir'))
# invalid suffix
print(find_files('.', 'unvaliddirec'))
# invalid path


