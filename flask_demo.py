from flask import Flask,render_template,request

#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route("/")
def greeting():
    return """<center><h1 style='color:red'>Welcome to Jenkins Tutorial Part 3</h1>
		<b><p>What is CICD?
		<p>Why do we need it?
		<p>Demo Video to see CICD </b>
	</center>"""


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
