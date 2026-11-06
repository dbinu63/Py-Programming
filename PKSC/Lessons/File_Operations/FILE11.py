def main():
    f = open(r"/Users/don/Downloads/School/code/py/FILE/neil.txt", "r")
    content = f.read()
    f.close()

    result = ""
    upper = True
    for char in content:
        if upper: 
            result += char.upper()
        else: 
            result += char.lower()

        upper = (char == " ")

    f = open(r"/Users/don/Downloads/School/code/py/FILE/mycopy.txt", "w")
    f.write(result)

    f.close()

if __name__ == "__main__":
    main()