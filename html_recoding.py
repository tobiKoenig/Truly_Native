import os 
import glob

Path=raw_input("Define Path: ")
count=0
for filename in glob.glob(os.path.join(Path, '*.txt')):
	f=filename
	count +=1
	print "iteration:" count 
	name=os.path.splitext(f)[0]
	os.rename(f,name+".html")
