def main(): 
    with open(r"/Users/don/Downloads/School/code/py/FILE/bird.jpg", "rb") as f:
        content = f.read()
        print(content[:50])

        

if __name__ == "__main__":
    main()