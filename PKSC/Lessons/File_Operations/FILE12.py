import csv

def main():
    students = [
        ["Roll No.", "Name", "Marks"],
        [101, "Jack", 85],
        [102, "Alice", 92],
        [103, "David", 78]
    ]

    f = open(r"/Users/don/Downloads/School/code/py/FILE/students.csv", "w", newline="")
    wr = csv.writer(f)
    wr.writerows(students)
    f.close()

if __name__ == "__main__":
    main()