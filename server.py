from flask import Flask, render_template ,request,session
app = Flask(__name__) 
app.secret_key="secret_key"
@app.route('/')
def index():
    return render_template('index.html')  

@app.route ('/summit_survey', methods=['POST'])
def result():
    session['name']=request.form['Name']
    session['selected_language']= request.form['FavoriteLanguage']
    session['location']=request.form['Dojolocation']
    session['comment']=request.form['Comments']
    return render_template("result.html", language=session['selected_language'], location=session['location'], name=session['name'], comment=session['comment'])



if __name__=="__main__":
    app.run(debug=True)    