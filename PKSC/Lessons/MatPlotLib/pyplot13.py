import matplotlib.pyplot as plt

def main(): 
    marks = [83, 27, 94, 56, 72, 83, 19, 67, 94, 41, 100, 56, 34, 87, 12, 72, 98, 46, 67, 90]

    plt.hist(marks, bins=5, color="red", edgecolor="black")

    plt.title("Distribution of Exam Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    plt.show()

if __name__ == "__main__":
    main()