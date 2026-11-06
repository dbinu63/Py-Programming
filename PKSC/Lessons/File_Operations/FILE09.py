def main():
    content = input("Enter input: ")

    f = open(r"/Users/don/Downloads/School/code/py/FILE/lmno.txt", "w")
    f.write(content)

    f.close()

if __name__ == "__main__":
    main()