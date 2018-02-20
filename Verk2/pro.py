from flask import *
from Controller import *

app = Flask(__name__)

if __name__ == "__main__":
    cont = Controller(Module("data.json"), View(), app)

    cont.module.writeData(
        0,
        Book(
            0,
            "Fifty Shades Of Red",
            "It's a book... That lists fifty shades of red",
            "BodyPen"
        )
    )
    cont.module.writeData(
        1,
        Book(
            1,
            "Book #2",
            "This is book number 2 in our catalog",
            "Author #2"
        )
    )
    cont.module.writeData(
        2,
        Book(
            2,
            "Insert Title Here",
            "Insert Description Here",
            "Insert Author Here"
        )
    )

    cont.module.writeData(3, Book(3))

    cont.generateRoute("/", "intro.html", None)
    for x in range(len(cont.module.getType(Book))):
        cont.generateRoute("/" + str(x), "info.html", {"BookDesc": cont.module.getData(x, Book).description})

    app.run(host='0.0.0.0')
