from flask import Flask, request, redirect, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return render_template('result.html', short_url=short_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
