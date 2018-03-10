from flask import *
from config import Config
from flask_sqlalchemy import SQLAlchemy
from forms import SearchForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Seller {}>'.format(self.name)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True , nullable=False)
    price = db.Column(db.Integer, nullable=False)
    seller = db.Column(db.Integer, db.ForeignKey("seller.id"), nullable=False)

    def __repr__(self):
        return '<Product {} {}>'.format(self.name, self.price)

#db.create_all()
#db.session.add(Seller(name="Billy Maze"))
#db.session.add(Seller(name="Khajiit With Nice Wares"))
#db.session.add(Seller(name="Hagkaup"))
#db.session.add(Product(name="FlexTape!", price=1300, seller=1))
#db.session.add(Product(name="ComboWambo!", price=2500, seller=1))
#db.session.add(Product(name="Moon Sugar", price=15000, seller=2))
#db.session.add(Product(name="Badger Fur", price=3450, seller=2))
#db.session.add(Product(name="Nammibar", price=100000, seller=3))
#db.session.add(Product(name="Eitthvað sem var ekki til í Bónus", price=23000, seller=3))
#db.session.commit()

@app.route('/', methods=['POST','GET'])
def hello_world():
    form = SearchForm()
    if form.validate_on_submit():
        print(list(filter(lambda x: x is not None, [x if form.productName.data.lower() in x.name.lower() else None for x in list(Product.query.all())])))
        return render_template("searchResults.html", len=len, prods=list(filter(lambda x: x is not None, [x if form.productName.data.lower() in x.name.lower() else None for x in list(Product.query.all())])), Seller=Seller)
    else:
        return render_template("index.html", form=form)


app.run("0.0.0.0", port=8080)