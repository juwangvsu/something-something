# change the jpeg file name to ####.jpg or ######.jpg
# usage: python $ fn6|fn4
# input 20bn-something-something-v2-frames/ all folders
import glob
import os
import sys
#vfolder_l=glob.glob('test2/*')
print(sys.argv)
#exit()
vfolder_l=glob.glob('20bn-something-something-v2-frames/*')
for i in range(len(vfolder_l)):
    vjpgs=glob.glob(vfolder_l[i]+'/*')
    for j in range(len(vjpgs)):
        fnl = vjpgs[j].split('/')
        fnseq=fnl[2].split('.')[0]
        if sys.argv[1]=='fn6':
            s1 = f'{int(fnseq):06d}'
        else:
            s1 = f'{int(fnseq):04d}'

        newfnl=fnl[0]+'/'+fnl[1]+'/'+s1+'.jpg'
        os.rename(vjpgs[j], newfnl)
