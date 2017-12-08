from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

headings = []
entries = []

@app.route('/', methods=['POST', 'GET'])
def blog_posts():
    
    if request.method == 'POST':
        heading = request.form['heading']
        entry = request.form['entry']
        headings.append(heading)
        entries.append(entry)

    return render_template('blog.html', title="BuildABlog", headings=headings, entries=entries)


app.run()