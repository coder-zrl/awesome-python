from flask import Flask
app=Flask(__name__)
@app.route('/')

def helloworld():
    return 'helloworld!'

@app.route('/user',methods=['GET','POST'])

def hello_user():
    return 'hello user'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8081)
