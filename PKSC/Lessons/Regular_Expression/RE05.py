import re

def main(): 
    str = "abc ab abbc abcabc aa abbbbc ac aabbc"

    result = re.findall("ab+c", str)
    print(result)

    result = re.findall("ab*c", str)
    print(result)

if __name__ == "__main__":
    main()