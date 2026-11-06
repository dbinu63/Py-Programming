# WAP to find out transacts from a list of transactions where the amount is most than 1000

def main():
    trans = [
        {"id": 101, "amt": 25},
        {"id": 102, "amt": -140},
        {"id": 103, "amt": 1900},
        {"id": 104, "amt": -200},
        {"id": 105, "amt": 50},
        {"id": 106, "amt": 100},
        {"id": 107, "amt": 2500}
    ]

    over_1k = list(filter(lambda t: t["amt"] > 1000, trans))
    print(trans)
    print()
    print(over_1k)

if __name__ == "__main__":
    main()