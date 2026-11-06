def main(): 
    f = open(r"/Users/don/Downloads/School/code/py/FILE/abc.txt", "r")

    content = f.read()
    # print(content)

    words = content.split() # this is a string method, not a file one
    print(len(words)) # number of words
    print(len(content)) # number of chars

    content = f.readlines()
    print(len(content)) # number of lines

    f.close()

if __name__ == "__main__":
    main()