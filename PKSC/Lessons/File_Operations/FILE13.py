import json

def main():
    with open(r"/Users/don/Downloads/School/code/py/FILE/student.json", "r") as f:
        s = json.load(f)

        print("Name:", s["name"])
        print("- - - - - - - - - - -")
        for i in range(len(s["subjects"])):
            subject = s["subjects"][i]
            mark = s["marks"][i]
            spaces = 7 - len(subject)
            print(subject, " " * spaces, "|   ", mark)

if __name__ == "__main__":
    main()