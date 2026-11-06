import re

def main(): 
    str = "cat c t cannot c_t ct cut c7t, cantt, cctv"

    result = re.findall("c.t", str)
    print(result)

    result = re.findall("c+t", str) # checks for repetition of c character
    print(result)



if __name__ == "__main__":
    main()