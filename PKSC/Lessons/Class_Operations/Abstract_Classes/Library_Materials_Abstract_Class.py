from abc import ABC, abstractmethod

class SearchMaterial(ABC):
    def __init__(self, material_id, title):
        self.material_id = material_id
        self.title = title

    @abstractmethod
    def disp(self):
        pass


class Book(SearchMaterial):
    def __init__(self, material_id, title, author, ISBN, pages, cost):
        super().__init__(material_id, title)

        self.author = author
        self.ISBN = ISBN
        self.pages = pages
        self.cost = cost

    def disp(self):
        print(f"Book ID: {self.material_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Pages: {self.pages}")
        print(f"Cost: ${self.cost:.2f}")
        print("-" * 30)
        print()


class Journal(SearchMaterial):
    def __init__(self, material_id, title, publisher, topic):
        super().__init__(material_id, title)

        self.publisher = publisher
        self.topic = topic

    def disp(self):
        print(f"Journal ID: {self.material_id}")
        print(f"Title: {self.title}")
        print(f"Publisher: {self.publisher}")
        print(f"Topic: {self.topic}")
        print("-" * 30)
        print()


def main():
    b1 = Book(
        "B1001",
        "The Adventures of Sherlock Holmes",
        "Sir Arthur Conan Doyle",
        "1234567",
        270,
        15.99
    )

    j1 = Journal(
        "J1001",
        "Journal of American Health and Wellness, Issue #59",
        "Journal of American Health and Wellness",
        "The Impact of Sickle Cell Disease in South Africa"
    )

    b1.disp()
    j1.disp()


if __name__ == "__main__":
    main()