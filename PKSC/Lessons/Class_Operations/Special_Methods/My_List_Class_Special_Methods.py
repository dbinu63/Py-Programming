from __future__ import annotations as an

class MyList:
    def __init__(self, *args):
        self.data = []

        if len(args) == 1:
            if isinstance(args[0], list):
                for n in args[0]:
                    self.data.append(n)
            elif isinstance(args[0], MyList):
                for n in args[0].data:
                    self.data.append(n)
            elif isinstance(args[0], int):
                self.data.append(args[0])
            else:
                print("Invalid data.")
        elif len(args) > 1:
            for n in args:
                self.data.append(n)
        else:
            pass

    def disp(self, sep=", "):
        length = len(self.data) - 1

        if len(self.data) == 0:
            print(f"No data to display")
        else:
            print("Data: ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            for e in self.data:
                if length != 0:
                    print(f"{e}, ", end=sep)
                else:
                    print(f"{e}")

                length -= 1

    @property
    def Count(self):
        return len(self.data)

    def __eq__(self, n: MyList):
        if self.Count != n.Count:
            return False

        for i in range(self.Count):
            if self.data[i] != n.data[i]:
                return False
        else:
            return True

    def __getitem__(self, index):
        if index not in range(len(self.data)):
            raise IndexError("Invalid index entered")
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

def main():
    p = MyList()
    p.disp()
    print()


    q = MyList(10)
    q.disp()
    print()

    r = MyList(11, 22, 33)
    r.disp()
    print()

    s = MyList([1, 2, 3, 4])
    s.disp()
    
    print()

    t = MyList(r)
    t.disp()
    print()

    if r == t:
        print("R and T are the same")

    print(f"{r[2]}")


if __name__ == "__main__":
    main()