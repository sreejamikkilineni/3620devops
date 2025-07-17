from flask import Flask,render_template,request 
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('myForm.html')
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    return render_template('greetings.html',name=username)
if __name__=='__main__':
    app.run(debug=True)