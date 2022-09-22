from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tort.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qtyprisoner = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article &r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST', 'GET'])
def calc():
    return render_template('calc.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
   return render_template('result.html')

@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')

        except:
            return "При добавлении статьи произошла ошибка"

    else:
        return render_template('create_article.html')

@app.route('/posts/<int:id>/post_update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form["title"]
        article.intro = request.form["intro"]
        article.text = request.form["text"]

        try:
            db.session.commit()
            return redirect('/posts')

        except:
            return "При редактировании статьи произошла ошибка"

    else:
        article = Article.query.get(id)
        return render_template('post_update.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    articles=Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)

@app.route('/posts/<int:id>')
def post_detail(id):
    article=Article.query.get(id)
    return render_template('post_detail.html', article=article)
@app.route('/posts/<int:id>/del')
def post_del(id):
    article=Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'При удалении статьи произошла ошибка'




@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page " + name + " - " + str(id)


if __name__ == '__main__':
    app.run(debug=True)
