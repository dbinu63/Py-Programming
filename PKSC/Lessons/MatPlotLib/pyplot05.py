import matplotlib.pyplot as plt

def main(): 
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]

    plt.plot(x, y, marker="o")

    plt.xlim(0, 6)
    plt.ylim(0, 35)

    plt.xticks([1, 2, 3, 4, 5])
    plt.yticks([0, 10, 20, 30, 40])

    plt.show()

if __name__ == "__main__":
    main()