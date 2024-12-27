from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/current_time')
def current_time():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return render_template('current_time.html', current_time=formatted_now)


if __name__ == '__main__':
    app.run(debug=True)
