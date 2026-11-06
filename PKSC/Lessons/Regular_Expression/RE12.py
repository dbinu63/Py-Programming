import re

def main(): 
    # str = "ABC123" # only result 1
    # str = "123AB" # only results 1 & 2
    str = "123456" # all results

    result1 = re.search(r"\d+", str)
    result2 = re.match(r"\d+", str)
    result3 = re.fullmatch(r"\d+", str)

    print(result1)
    print(result2)
    print(result3)

if __name__ == "__main__":
    main()