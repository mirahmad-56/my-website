from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/help')
def help():
    return render_template('help.html')
@app.route('/maths')
def maths():
    return render_template('maths.html')
@app.route('/science')
def science():
    return render_template('science.html')
@app.route('/programing')
def programing():
    return render_template('programing.html')




if __name__ == '__main__':
    app.run(debug=True)