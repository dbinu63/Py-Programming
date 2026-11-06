import re

def main(): 
    str = "Account Number: SBI1234, Amount: 45000"

    result = re.findall(r"\d+", str) # numbers
    print(result)
    result = re.findall(r"\w+", str) # words
    print(result)

if __name__ == "__main__":
    main()