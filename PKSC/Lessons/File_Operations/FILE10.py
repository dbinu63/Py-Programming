def main():
    content = input("Enter input: ")
    result = ""

    for char in content:
        if char in "aeiouAEIOU":
            result += char.upper()
        else:
            result += char.lower()

    f = open(r"/Users/don/Downloads/School/code/py/FILE/lmno.txt", "w")
    f.write(result)

    f.close()

if __name__ == "__main__":
    main()