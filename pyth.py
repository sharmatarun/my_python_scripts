import os
import errno
import shutil
src_path=r'C:\\'
dst_path=r'H:\\programming\\languages\\C\\'
list1=["languages","comp_programming"]
list2=["C","PYTHON"]
def make_sure_path_exists(str1,str2):
    try:
        if str2=="languages":
            for str in list2:
                os.makedirs(str1+"/"+str2+"/"+str)
        else:
            os.makedirs(str1+"/"+str2)
    except OSError as exception:
        if exception.errno !=errno.EEXIST:
            raise

for str in list1:
    make_sure_path_exists("programming",str)

def c_ko_alag(dir_src,dir_dst):
    for ROOT,DIR,files in os.walk(dir_src):
        for file in files:
            extension=os.path.splitext(file)[1]
            if extension=='.c':
                src_file=os.path.abspath(os.path.join(ROOT,file))
                dst_file=os.path.join(dir_dst,file)
                shutil.copy(src_file,dst_file)
            else:
                print file

c_ko_alag(src_path,dst_path)



