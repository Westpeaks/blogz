from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Build-a-Blog2:12Kamelz@localhost:8889/Build-a-Blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    
    if request.method == 'POST':
        entry_name = request.form['title']
        entry_body = request.form['body']
        new_entry = Blog(entry_name, entry_body)
        db.session.add(new_entry)
        db.session.commit()
        return redirect("/single_post?id="+ str(new_entry.id))
    
    return render_template('new_post.html')

@app.route('/single_post', methods =['POST','GET'])
def blog():
    if request.args:
        blog_id = request.args.get("id")
        blog_entry = Blog.query.get(blog_id)
    return render_template('single_post.html', blog=blog_entry)
        
@app.route('/', methods=['POST', 'GET'])
def index():
        
    entries = Blog.query.all()

    return render_template('blog.html', entries=entries)

if __name__ == '__main__':
    app.run()