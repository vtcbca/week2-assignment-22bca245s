#script 7
f=["program.c","stadio.c","sample.c","a.py","math.py","hpp.py"]
f1=[s for s in f if ".c" in s]
print(f1)
f_replc=[s.replace(".c",".py") for s in f]
print(f_replc)
