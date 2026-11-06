import re

def main(): 
    str = "Rahul works at SBI in India"

    result = re.findall(r"\b[A-Z][a-z]+\b", str)
    print(result)

    result = re.findall(r"\b[A-Z]+[a-z]+\b", str)
    print(result)

    result = re.findall(r"\b[A-Z]+[a-z]*\b", str)
    print(result)

if __name__ == "__main__":
    main()