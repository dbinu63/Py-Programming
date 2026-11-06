import matplotlib.pyplot as plt

def main(): 
    days = [1, 2, 3, 4, 5]
    city1 = [25, 30, 25, 27, 21]
    city2 = [32, 35, 31, 28, 30]

    plt.plot(days, city1, marker="o", color="olive", label="Houston")
    plt.plot(days, city2, marker="*", color="pink", label="Dallas")

    plt.xlim(0, 6)
    plt.ylim(10, 40)

    plt.xticks([0, 1, 2, 3, 4, 5, 6])
    plt.yticks([10, 15, 20, 25, 30, 35, 40])

    plt.title("Temperature Comparison Between Two Cities")
    plt.xlabel("Day")
    plt.ylabel("Temperature")

    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()