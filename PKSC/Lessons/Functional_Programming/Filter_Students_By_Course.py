def main():
    students = [
        {"scode": 101, "name": "David", "course": ["C", "Python"]},
        {"scode": 101, "name": "Sarah", "course": ["HTML", "CSS"]},
        {"scode": 101, "name": "John", "course": ["Python", "C", "C++"]},
        {"scode": 101, "name": "James", "course": ["Java", "Python"]},
        {"scode": 101, "name": "Lucy", "course": ["Ruby", "JavaScript"]},
    ]

    c_students = list(filter(lambda s: "C" in s["course"], students))

    print(c_students)

if __name__ == "__main__":
    main()