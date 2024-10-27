from flask import Flask,request,url_for,render_template

app=Flask (__name__)

@app.route ('/')
def hello_world():
    title1="Python3"
    content1="hello python,kalof!"
    return render_template('index1.html',title=title1,content=content1)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)