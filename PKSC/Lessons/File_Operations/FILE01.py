def main(): 
    f = open(r"/Users/don/Downloads/School/code/py/FILE/abc.txt", "r")

    content = f.read()

    print(content)

    f.close()

if __name__ == "__main__":
    main()