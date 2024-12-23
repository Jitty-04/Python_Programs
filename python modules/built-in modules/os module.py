import os #os used to interact with os

#working with dir

#getcwd:get current working directory
# current_directory=os.getcwd()
# print(f'current working directory:{current_directory}')
#
# #listdir():list all files and directories in the specific path
# #r:raw string:used to remove unicode escape errors in program
# path=r'C:\Users\jitty\PycharmProjects\python_basics\Looping'
# items=os.listdir(path)
# print(items)#display list

# #mkdir():create a directory
# new_dir=r'C:\Users\jitty\PycharmProjects\python_basics\sampledir'
# os.mkdir(new_dir)
# print(f'Directory {new_dir} created')

#rmdir(): remove directory(only works if directory is empty)
# dir_remove=r'C:\Users\jitty\PycharmProjects\python_basics\sampledir'
# os.rmdir(dir_remove)
# print(f'Directory {dir_remove} removed')


#working with files
import os
from os import remove

#specify the path to check
path=r'C:\Users\jitty\PycharmProjects\python_basics\python modules\built-in modules\calendermodule.py'
if os.path.exists(path):
    print(f'path {path} exists')
else:
    print(f'path {path} does not exist')


#remove
file_remove=r'C:\Users\jitty\PycharmProjects\python_basics\removefile.py'
if os.path.exists(file_remove):
    remove(file_remove)
    print(f'file {file_remove} removed')
else:
    print(f'file {file_remove} does not exist')



