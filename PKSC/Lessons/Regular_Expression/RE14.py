import re

def main(): 
    str = "13-11-1970"

    pattern = r"(\d{2})-(\d{2})-(\d{4})"
    result = re.fullmatch(pattern, str)
    if result:
        print(result.group(0))
        print("Day:", result.group(1))
        print("Month:", result.group(2))
        print("Year:", result.group(3))

        print(result.groups())

if __name__ == "__main__":
    main()