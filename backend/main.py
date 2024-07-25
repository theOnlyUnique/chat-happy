from flask import Flask, request
import dashscope
# 配置跨域允许
from flask_cors import CORS # 添加这行导入
# from function.fun import *
from data.data import *
# 首先注册通义千问账号，获得 DASHSCOPE_API_KEY
# 替换下方的 api_key
# 参考：https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-qianwen-7b-14b-72b-quick-start?spm=a2c4g.11186623.0.0.18159b6eCAijjm

dashscope.api_key = api_key # 替换为你自己的 DASHSCOPE_API_KEY

app = Flask(__name__)
CORS(app,supports_credentials=True) # 添加这行，启用CORS支持

@app.route('/get-response')
def index():
    print('server Runner!')
    queryId = request.args.get("queryId")
    query = request.args.get("query")
    print("打印查询请求,ID：{},content: {}".format(queryId,query))
    response,hashValue = getResponse("liuqidong",queryId,query)
    print("打印",hashValue)
    return {
        'id': queryId,
        'query': query,
        'response': response,
        'hashValue':hashValue
    }

@app.route('/import-chat')
def getChat():
    print('用户请求聊天！')
    hashValue = request.args.get("hashValue")
    data= getData(hashValue)
    print("打印获取结果",data)
    return {
        'conversationList':data
    }

if __name__=="__main__":
    print("执行main")
    app.run(host=IP, port=PORT) # host 换成你自己的本地 ip。另外 frontend 蓝河应用代码中 getResponse 方法也要对应替换成自己的 ip
