from flask import Flask, request, render_template
app = Flask(__name__)

tweets = []
@app.route("/")
def hello():
    return app.send_shapes_file('index.html')
@app.route("/api/hakk", methods=["POST"])
def receive_hack():
	name = request.form['name']
	hakk = request.form['hakk']
	tweets.append({'name': name, 'hakk': hakk})
	print(tweets)
	return "Success!"

@app.route('/dope')
def show_tweets():
	return render_template('tweets.html', tweets=tweets)

if __name__ == "__main__":
    app.run()