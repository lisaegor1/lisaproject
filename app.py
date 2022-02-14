#!flask/bin/python
from flask import Flask

UPLOAD_FOLDER = '/home/yehor/tz'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#app = Flask(__name__)

#UPLOAD_DIRECTORY = "/home/yehor/TZ/uploads"

#@app.route('/sg')
#def index():
#    return render_template("sg.html")


#if __name__ == "__main__":
#    app.run(debug=True)
