import re

def main(): 
    str = "Python is one of the most efficient languages"

    result = re.findall("^Python", str)
    print(result)

    result = re.findall("languages$", str)
    print(result)



if __name__ == "__main__":
    main()