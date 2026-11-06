def main(): 
    f = open(r"/Users/don/Downloads/School/code/py/FILE/abc.txt", "r")

    print(f.tell())
    content = f.read(10)
    print(content)
    print(f.tell()) # shows where the cursor is in the file
    content = f.read(3)
    print(content)
    print(f.tell())

    f.seek(0)
    print(f.tell())
    content = f.read(4)
    print(content)

    f.close()

if __name__ == "__main__":
    main()