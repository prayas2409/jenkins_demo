from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def greeting():
    return """<center><h1 style='color:blue'>Welcome to Jenkins Tutorial Part 4</h1>
		<b><p>What is Server?
		<p>Why do we need it?</b>
	</center>"""


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
