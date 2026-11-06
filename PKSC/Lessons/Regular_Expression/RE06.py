import re

def main(): 
    str = "color, colour, colouur"

    result = re.findall("colou*r", str)
    print(result)

    result = re.findall("colou+r", str)
    print(result)

    result = re.findall("colou?r", str)
    print(result)

if __name__ == "__main__":
    main()