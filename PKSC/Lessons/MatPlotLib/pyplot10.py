import matplotlib.pyplot as plt

def main(): 
    subject = ["C", "Python", "VB", "Java"]
    marks = [85, 78, 92, 88]

    # py doesn't work with the typical 0-255 vals for RGB, but rather works with decimals 0-1. For example, R(200), G(50), B(250) should be written as (in decimals, set in a tuple) 200/255, 50/255, 250/255
    plt.bar(subject, marks, color=["#29C287", "#DE9E14", "#5414DE", "#DE1439"]) # accepts hexdec
    plt.title("Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0, 100)

    plt.show()

if __name__ == "__main__":
    main()