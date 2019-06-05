from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/config')
def about():
    return render_template('config.html')

@app.route('/evaluation')
def evaluation():
    return render_template('layoutEval.html')

@app.route('/evaluation/theories')
def theory():
    return render_template('theory.html')

@app.route('/evaluation/emotions')
def emotion():
    return render_template('emotions.html')

@app.route('/evaluation/rules')
def rules():
    return render_template('rules.html')

if __name__ == '__main__':
    app.run(debug=True)