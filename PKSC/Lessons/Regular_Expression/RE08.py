import re

def main(): 
    str = "cat cot cut cit cet"

    result = re.findall("c[ao]t", str)
    print(result)

if __name__ == "__main__":
    main()