import matplotlib.pyplot as plt

def main(): 
    subject = ["C", "Python", "VB", "Java"]
    marks = [85, 78, 92, 88]

    plt.bar(subject, marks, color="skyblue")
    plt.title("Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0, 100)

    plt.show()

if __name__ == "__main__":
    main()