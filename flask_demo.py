from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def greeting():
    return """<center><h1 style='color:green'>Welcome to Jenkins Tutorial Part 2</h1>
		<b><p>What is Jenkins?
		<p>What is CICD?</b>
	</center>"""


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
