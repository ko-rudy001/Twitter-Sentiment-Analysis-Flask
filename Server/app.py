import  util
from flask import Flask, render_template, request
import os

app = Flask(__name__)

picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder


@app.route("/", methods=["GET","POST"])
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'twitter.png')

    if request.method == "POST":

        text = request.form["inp"]
        val = util.get(text)

        if val == 0:
            return render_template('index.html', user_image=pic1, message="Neutral Response😐😐")
        elif val == 1:
            return render_template('index.html', user_image=pic1, message="Positive Response😊😊")
        else:
            return render_template('index.html', user_image=pic1, message="Negative Response🥹🥹")

    return render_template('index.html', user_image=pic1)


if __name__ == "__main__":
    app.run()