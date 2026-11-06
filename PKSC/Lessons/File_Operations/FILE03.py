def main(): 
    f = open(r"/Users/don/Downloads/School/code/py/FILE/abc.txt", "r") # default is read mode, so technically 2nd param isn't required, but it's better if you keep it

    content = f.readlines()
    print(content)

    f.close()

if __name__ == "__main__":
    main()