#!flask/bin/python
import os

from flask import Flask, request, abort, jsonify, send_from_directory, render_template



UPLOAD_DIRECTORY = "/home/yehor/TZ/uploads"


app = Flask(__name__)


@app.route('/sg')
def index():
    return render_template("sg.html")


@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
