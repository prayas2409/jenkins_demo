from flask import Flask,render_template,request

#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route("/")
def greeting():
    return "<h1 style='color:red'>Welcome to Jenkins Tutorial</h1>"


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
