#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask, render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer/test')
def customer_test():
    """
    data = {}
    data['name'] = "ESN1"
    data['gender'] = "男"
    """
    
    data = {'name':"ESN", 'gender':"男", "age":20}

   
    return render_template("test.html", data = data)

@app.route('/customer/list')
def customer_list():    
    data = [{'name':"ESN1", 'gender':"男", "age":21},
            {'name':"ESN2", 'gender':"男", "age":22},
            {'name':"ESN3", 'gender':"女", "age":23},
            {'name':"ESN4", 'gender':"男", "age":24},
            {'name':"ESN5", 'gender':"男", "age":25},]
   
    return render_template("list.html", data = data)

#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)