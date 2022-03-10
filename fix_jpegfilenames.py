# change the jpeg file name to ####.jpg
# input 20bn-something-something-v2-frames/ all folders
import glob
import os
#vfolder_l=glob.glob('test2/*')
vfolder_l=glob.glob('20bn-something-something-v2-frames/*')
for i in range(len(vfolder_l)):
    vjpgs=glob.glob(vfolder_l[i]+'/*')
    for j in range(len(vjpgs)):
        fnl = vjpgs[j].split('/')
        fnseq=fnl[2].split('.')[0]
        s1 = f'{int(fnseq):04d}'
        newfnl=fnl[0]+'/'+fnl[1]+'/'+s1+'.jpg'
        os.rename(vjpgs[j], newfnl)
