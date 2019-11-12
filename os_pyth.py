#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os 
print(os.getcwd()) 
# To print absolute path on your system 
# os.path.abspath('.')  
  
# To print files and directories in the current directory 
# on your system 
# os.listdir('.') 
topdown − If optional argument topdown is True or not specified,
directories are scanned from top-down.
If topdown is set to False, directories are scanned from bottom-up.
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

