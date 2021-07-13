from flask import Flask

app = Flask(__name__)

@app.route("/")
def Start():
	return "여기는 Main Page입니다..."

@app.route("/Smart")
def Test1():
    return "여기는 smart Page입니다..."

@app.route("/hanga")
def Test2():
    return "여기는 한가람  Page입니다..."

if __name__ == "__main__":
	app.run(host="0.0.0.0")

