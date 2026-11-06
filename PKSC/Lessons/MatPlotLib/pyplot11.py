import matplotlib.pyplot as plt

def main(): 
    hours_studied = [1, 2, 3, 4, 5, 6, 7]
    marks = [25, 40, 50, 62, 78, 85, 93]

    plt.scatter(hours_studied, marks, color="purple", alpha=1, s=50)
    # alpha is transparency, s is scale of scatter points

    plt.title("Hours Studied v Marks")
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks")

    plt.show()

if __name__ == "__main__":
    main()