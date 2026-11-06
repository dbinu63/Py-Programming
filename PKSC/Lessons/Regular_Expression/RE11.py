import re

def main(): 
    str = """
Salary: 45000,
Rent: 11000
Electricity: 2500
Food: 6000
"""

    amounts = re.findall(r"\d+", str)
    print(amounts)

if __name__ == "__main__":
    main()