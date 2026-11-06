import re

def main(): 
    str1 = "To have no enemies, one must not be a meanie - Sun Tzu, The Art of War"
    result = re.search("enemies", str1)
    print(result);

    str2 = "One small step for man, one giant leap for mankind"
    result = re.search("leap", str2)
    print(result);
    print(result.group())
    print(result.start())
    print(result.end())



if __name__ == "__main__":
    main()