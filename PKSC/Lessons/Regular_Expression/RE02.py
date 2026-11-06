import re

def main(): 
    str = "Python is one of the most efficient languages. I am learning python. Functions are important in Python."

    result1 = re.search("Python", str)
    result2 = re.findall("Python", str)
    result3 = re.findall("Python", str, flags=re.IGNORECASE) # can use re.I as well
    result4 = re.findall("Python1", str, flags=re.IGNORECASE) # can use re.I as well

    print(result1) # search returns first matching str as an object
    print(result1.group())
    print(result2)
    print(result3) # findall returns all matching strs as a list
    print(result4)



if __name__ == "__main__":
    main()