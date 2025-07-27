from flask import Flask,render_template
project=Flask(__name__)
@project.route('/')
def home():
    return render_template('index.html')

@project.route('/feedback')
def feedback():
    return render_template('feedback.html')

@project.route('/login')
def login():
    return render_template('login.html')
@project.route('/education')
def education():
    return render_template('education.html')

@project.route('/help')
def help():
    return render_template('help.html')
@project.route('/maths')
def maths():
    return render_template('maths.html')
@project.route('/science')
def science():
    return render_template('science.html')
@project.route('/programing')
def programing():
    return render_template('programing.html')




if __name__ == '__main__':
    project.run(debug=True)