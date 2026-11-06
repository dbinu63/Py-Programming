# import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    hours = [0, 1, 2, 3, 4, 5]
    temp = [45, 60, 65, 71, 67, 60]

    plt.plot(hours, temp, color="green", marker="o", linestyle="-",linewidth=2, markersize=7,label="Temperature")
    plt.show()
    # marker accepts: 'o', '*', '^', 's', 'x'
    # linestyle accepts: ':', '--', '-', '-.'

if __name__ == "__main__":
    main()