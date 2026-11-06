# add 20% to salary if it's > 10000, 50% if it's <= 10000

def main():
    employees = [
        {"ecode": 101, "name": "David", "salary": 12000},
        {"ecode": 102, "name": "Peter", "salary": 7000},
        {"ecode": 103, "name": "John", "salary": 15000},
        {"ecode": 104, "name": "Sarah", "salary": 10000},
        {"ecode": 105, "name": "James", "salary": 9000},
        {"ecode": 106, "name": "Lucy", "salary": 9000},
        {"ecode": 107, "name": "Charles", "salary": 11000},
    ]

    new_salary = list(map(lambda e: {"ecode": e["ecode"], "name": e["name"], "salary": int(e["salary"] * 1.2) if e["salary"]> 10000 else int(e["salary"] * 1.5)}   , employees))
    
    for e in new_salary:
        print(e)

if __name__ == "__main__":
    main()