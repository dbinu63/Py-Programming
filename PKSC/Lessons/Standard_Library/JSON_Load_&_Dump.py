import json

def main():
    x = '{"name" : "Don", "age" : 19, "course" : ["C", "Java", "Python"]}'
    y = json.loads(x)

    print(y)
    print(y["name"])
    print(y["age"])

    x = {"name" : "John", "dept" : "HR", "desig" : "Manager", "salary" : 20000}
    y = json.dumps(x)

    print(y)

if __name__ == "__main__":
    main()