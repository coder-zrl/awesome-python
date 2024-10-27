from flask import Flask,request
app=Flask(__name__)
@app.route('/')

def hello_world():
    return 'hello world!'

@app.route('/user',methods=['GET','POST'])

def hello_user():
    return 'hello user'

@app.route('/users/<uid>')
def user_id(uid):
    return 'hello user'+uid

@app.route('/query_user')
def query_user():
    uid=request.args.get('uid')
    return 'query user'+uid

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)