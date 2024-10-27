from flask import Flask,request,url_for,render_template

app=Flask (__name__)

@app.route ('/')
def hello_world():
    title1='python'
    content1='hello python'
    return render_template('index.html',title=title1,content=content1)

@app.route('/user',methods=['GET','POST'])
def hello_user():
    return "hello user "

@app.route('/users/<uid>')
def user_id(uid):
    return 'hello user'+uid

@app.route('/query_user')
def query_user():
    uid=request.args.get('uid')
    return 'query user'+uid

@app.route ('/query_url' )#反向路由
def query_url():
    return "query url: "+ url_for('query_user')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)