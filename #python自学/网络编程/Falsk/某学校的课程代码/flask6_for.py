from flask import Flask,request,url_for,render_template

app=Flask (__name__)

@app.route ('/')
def hello_world() :
    title=" Python3"
    content= ["hello python","hello","hello kalof"]
    return render_template('index2.html',title=title,contents=content)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)