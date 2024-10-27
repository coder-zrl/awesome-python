from flask import Flask,request,url_for,render_template,flash

app=Flask (__name__)
app.secret_key='123'

@app.route ('/')
def hello_world() :
    title=" Python3"
    content= ["hello python","hello","hello kalof"]
    return render_template('index2.html',title=title,contents=content)

@app.route('/info')
def info():
    flash("hello python and li")
    return render_template("info.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)