with open("file_txt","r") as f:
    print(f.read())

# for each line separately

with open("file_txt","r") as f:
    for line in f:
        print(line,end="")


# we can send the path as actual path or the Relative Path
        

# write to a file
        
with open("newfile","w") as f:
    f.write("Hello world")
# the current content will be erased
    
#  "a" for append if we do not want to erase

with open("newfile","a") as f1:
    f1.write("Hello")