from flask import Flask,request,url_for,render_template,flash,abort

app=Flask (__name__)
app.secret_key='123'

@app.route ('/')
def hello_world() :
    title=" Python3"
    content= ["hello python","hello","hello kalof"]
    return render_template('index2.html',title=title,contents=content)

@app.route('/query_user')
def query_user():
    uid=request.args.get("uid")
    if int(uid):
        return "query user:"+ uid
    else:
        abort(500)

@app.errorhandler(500)
def not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)