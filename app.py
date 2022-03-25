from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', title="My Cool App", items = ["A", "B", "C"], x = 5)
if __name__ == '__main__':
    app.run(debug=True)