import re

def main(): 
    str = "A1 AB12 ABC123 ABCD1234"

    result = re.findall(r"\d{2}", str) # r means raw text, as opposed to f for formatted
    print(result)

    result = re.findall(r"\d{2,4}", str)
    print(result)

if __name__ == "__main__":
    main()