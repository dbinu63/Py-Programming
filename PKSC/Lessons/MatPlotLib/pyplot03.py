# import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    hours = [0, 1, 2, 3, 4, 5]
    temp = [45, 60, 65, 71, 67, 60]

    plt.plot(hours, temp, color="magenta", marker="o", linestyle=":",linewidth=2, markersize=7,label="Temperature")
    plt.title("Temperature of the Day")
    plt.xlabel("Hours")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()