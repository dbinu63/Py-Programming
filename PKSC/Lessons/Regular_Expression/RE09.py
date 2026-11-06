import re

def main(): 
    str = "A1 B2 C3 a4 b5 Z6"

    result = re.findall(r"[A-Z]", str)
    print(result)

    result = re.findall(r"[a-z]", str)
    print(result)

    result = re.findall(r"[0-9]", str)
    print(result)

    result = re.findall(r"[^0-9]", str)
    print(result)

if __name__ == "__main__":
    main()