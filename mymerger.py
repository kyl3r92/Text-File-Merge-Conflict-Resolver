print("test")
# Python code to
# demonstrate readlines()
import glob, os
for file in glob.glob("D:/UnityWorkspace/Pecker/**/*.cs", recursive=True):
    print(file)
    
    filename = file

    file1 = open(filename, 'r')


    Lines = file1.readlines() 

    begin = '<<<<<<< HEAD\n'
    mid = '=======\n'
    end = '>>>>>>> Upload before updating to 2019.4.8f1 (with dark theme)\n'

    action = "use"

    newfile = ""
      
    count = 0
    # Strips the newline character
    for line in Lines:
        
        if line == begin:
            print("found begin")
            action = "nothing"
        elif line == mid:
            print("found mid")
            action = "use"
        elif line == end:
            print("found end")
            action = "use"
        else:
            if action == "use":
                newfile += line

    file1.close()
    file2 = open(filename, 'w')
    file2.write(newfile)
    file2.close()
    print("done with " + file)
print("done!")
#print(newfile)