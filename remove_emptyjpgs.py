# change the jpeg file name to ####.jpg
# input 20bn-something-something-v2-frames/ all folders
import glob
import os
#vfolder_l=glob.glob('test2/*')
vfolder_l=glob.glob('20bn-something-something-v2-frames/*')
for i in range(len(vfolder_l)):
    vjpgs=glob.glob(vfolder_l[i]+'/*')
    if vjpgs==[]:
        continue
    if os.stat(vjpgs[0]).st_size <1:
        for j in range(len(vjpgs)):
            os.remove(vjpgs[j])

