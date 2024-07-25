from http import HTTPStatus
from flask import Flask, request
import dashscope

# 首先注册通义千问账号，获得 DASHSCOPE_API_KEY
# 替换下方的 api_key
# 参考：https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-qianwen-7b-14b-72b-quick-start?spm=a2c4g.11186623.0.0.18159b6eCAijjm

dashscope.api_key = 'xxx' # 替换为你自己的 DASHSCOPE_API_KEY

app = Flask(__name__)

@app.route('/get-response')
def index():
  print('收到请求')
  queryId = request.args.get("queryId")
  query = request.args.get("query")
  print(queryId)
  print(query)
  return {
    'id': queryId,
    'query': query,
    'response': getResponse(query),
  }

def getResponse(query):
  return call_with_messages(query)

# 通义千问开源模型：72b
def call_with_messages(query):
    messages = [
        {'role': 'user', 'content': query}]
    response = dashscope.Generation.call(
        'qwen1.5-72b-chat',
        messages=messages,
        result_format='message',  # set the result is message format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
        return response.output.choices[0].message.content
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return '出错了！'

if __name__ == '__main__':
  app.run(host='xxx', port='6432') # host 换成你自己的本地 ip。另外 frontend 蓝河应用代码中 getResponse 方法也要对应替换成自己的 ip
