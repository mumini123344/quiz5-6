from flask import Flask, redirect, url_for, render_template, request, session, app
from flask_sqlalchemy import SQLAlchemy
from Templates.main import bruh

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gveteneba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animelist.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class animelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    score = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f'{self.id}) Anime Name:{self.title}; Genre: {self.genre}; Score: {self.score}'


all_anime = animelist.query.all()
for each in all_anime:
    print(each)


@app.route('/animelist')
def anilist():
    return render_template('anime.html', all_anime=all_anime)


@app.route('/newanime', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        t = request.form['title']
        g = request.form['genre']
        s = request.form['score']
        ani = animelist(title=t, genre=g, score=float(s))
        db.session.add(ani)
        db.session.commit()
        return render_template('anime.html')


@app.route('/')
def home():
    all_anime = animelist.query.all()
    return render_template('home.html', all_anime=all_anime)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/<name>')
def userage(name):
    return f'Hello {name}'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


@app.route('/parse')
def scraped():
    scrap = bruh()
    return render_template('parsing.html', scrap=scrap)


if __name__ == "__main__":
    app.run(debug=True)
