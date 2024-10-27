from flask import Flask
import pandas as pd

app=Flask(__name__)
# app.debug=True
@app.route( '/')
def show_excel():
    df = pd.read_excel("环境数据.xls")
    table_html = df.to_html()
    print(table_html)
    return f'''
        <html>
            <body>
                <h1>学生信息表</h1>
                <div>{table_html}</div>
            </body>
        </html > 
'''

if __name__ == '__main__':
    app.run(host="192.168.1.100")