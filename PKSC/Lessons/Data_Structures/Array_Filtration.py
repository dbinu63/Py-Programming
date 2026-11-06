def main():
    a = ['mango', 'apple', 'banana', 'dragonfruit', 'apricot']
    x = []
    
    x = [y for y in a if y.startswith('a')]

    print(x)

if __name__ == "__main__":
    main()