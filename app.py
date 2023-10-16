from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','css', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_0159.JPG')
    return render_template("about.html", user_image = pic1)

@app.route("/projects")
def projects():
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'quickfoodspic.png')
    return render_template("projects.html", user_image = pic2)


if __name__ == '__main__':
    app.run(debug=True)