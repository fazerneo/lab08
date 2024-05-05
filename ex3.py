try:
    # Copyting text from foo.txt to bar.txt
    # Note: file bar.txt can be created with "w" as mode but "x" create mode helps us catch the error
    with open("foo.txt", "r") as textfile1, open("bar.txt", "x") as textfile2:
        copyline = textfile1.read()
        textfile2.write(copyline)
        print("copy sucess")
    
except FileNotFoundError:
    print("File foo.txt does not exist")

except :
    print("File bar.txt already exists")
    
