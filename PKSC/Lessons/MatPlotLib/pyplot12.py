import matplotlib.pyplot as plt

def main(): 
    subject = ["C", "Python", "VB", "Java"]
    marks = [30, 40, 20, 10]

    plt.pie(marks, labels=subject, colors=["red", "green", "blue", "yellow"], startangle=90, autopct="%1.1f%%")
    # red slice will start at 90 degree north of east
    
    plt.title("Marks Per Subject") 
    plt.show()

if __name__ == "__main__":
    main()