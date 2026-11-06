import matplotlib.pyplot as plt

def main(): 
    subject = ["C", "Python", "VB", "Java"]
    marks = [85, 78, 92, 88]
    colors = ["darkred", "olive", "indigo", "royalblue"]

    # PREDEFINED COLORS: 
    # red, green, blue, orange, yellow, coral, gold, magenta, brown, black, white, teal, lime, purple
    # cyan, pink, gray, navy, tomato, olive, salmon, indigo, royalblue, skyblue, darkred, chocolate

    plt.bar(subject, marks, color=colors) # can pass list into color
    plt.title("Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0, 100)

    plt.show()

if __name__ == "__main__":
    main()