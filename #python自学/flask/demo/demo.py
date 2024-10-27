from flask import Flask, render_template, request

# 创建应用程序
app = Flask(__name__)		# 生成应用实例


# @app.route('/')  # 创建路由，当访问到127.0.0.1:5000/会默认执行这个函数。
# # /代表请求名，浏览器末尾其实有这个/的，可以写成@app.route('/do')然后访问http://127.0.0.1:5000/do
# # 写一个函数处理浏览器发过来的请求,否则会404
# def indxe():  # 名字随意
#     return "你好，欢迎访问"  # 返回的数据-->响应


# 模板-->html，创建templates文件夹，引入render_template
# @app.route('/')
# def indxe():  # 名字随意
#     return render_template('hello.html')  # 会自动的找templates文件夹的hello.html


# 把一个变量发送到页面
# @app.route('/')
# def indxe():  # 名字随意
#     s='你好啊，臭狗屎!'
#     ls=['狂战士','狱血魔神','神思者','狗屎']
#     return render_template('hello.html',jay=s,list=ls)  # jay是瞎几把写的，这样就有了jay变量


# 通过一个案例学习如何从页面接收数据
# 登录验证
@app.route('/')
def indxe():  # 名字随意
    s='你好啊，臭狗屎!'
    ls=['狂战士','狱血魔神','神思者','狗屎']
    return render_template('login.html',jay=s,list=ls)  # jay是瞎几把写的，这样就有了jay变量
@app.route('/login',methods=['POST'])  # 写成post，否则找不到对应的处理
def logoin():  # 处理logo的请求
    # 接收到用户名和密码
    username=request.form.get('username')
    pwd=request.form.get('pwd')
    # request.args.get() 通过url传参
    if username=='abc' and pwd=='123456':
        return '成功'
    else:
        return render_template('login.html',mes='登陆失败，沟槽的')



if __name__ == '__main__':
    app.run()  # 启动应用程序
