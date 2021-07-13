from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
	return "<h2>에이치 원</h2>"	
	#return "Hello World"

if __name__ == "__main__":
	app.run(host="0.0.0.0")

