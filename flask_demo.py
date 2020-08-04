from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def greeting():
    return """<center><h1 style='color:green'>Welcome to Jenkins Tutorial Part 9</h1>
		<b><p>This is installation of Jenkins with github webhook
		</b>
	</center>"""


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
