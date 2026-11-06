import matplotlib.pyplot as plt
import matplotlib.colors as col

def main(): 
    # little system specific

    subject = ["C", "Python", "VB", "Java"]
    marks = [85, 78, 92, 88]
    colors = ["darkred", "olive", "indigo", "royalblue"]
    gradient = []

    for color in colors: 
        cmap = col.LinearSegmentedColormap.from_list("gradient", ["white", color])
        gradient.append(cmap(0.5)) # 0.5 sets color halfway across gradient, value must be passed

    plt.bar(subject, marks, color=gradient)
    plt.title("Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0, 100)

    plt.show()

if __name__ == "__main__":
    main()