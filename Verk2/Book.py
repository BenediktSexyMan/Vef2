class Book:
    def __init__(self, id, title="Undefined Title", description="Undefined Description", author="Undefined Author"):
        self.__title = title
        self.__description = description
        self.__author = author
        self.__ID = id

    @property
    def ID(self):
        return self.__ID

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def author(self):
        return self.__author

    @property
    def raw(self):
        return {"ID": self.ID, "title": self.title, "description": self.description, "author": self.author}

    def __repr__(self):
        return "Book{ " + self.title + " by " + self.author + " }"