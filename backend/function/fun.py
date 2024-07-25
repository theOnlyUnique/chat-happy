# 存放函数声明
import dashscope
from http import HTTPStatus
from data.data import MOUDLE_NAME
from dashscope.api_entities.dashscope_response import  Role
# 获取时间戳
from utils.getHashId import getTimeInteger
# 获取数据库信息
from utils.getDataBaseInfo import linkMysql,commitInfo
# 序列化 分序列化工具
from utils.Serialization import serialization,reSerialization
# 导入编码的家伙
from utils.coding import decode_unicode_sequences

messages=list()
hashId = "null"

#  预设prompt
def definePrompt():
    global messages
    Lawyer = {'role': Role.SYSTEM,
              'content': '你是一名专业的律师，请尽可能用律法方面的专有名词来回答我，并且对比较生僻的法律名词进行解释。'}
    mather = {'role': Role.SYSTEM,
              'content': '你是一名数学专家，你拥有渊博的数学知识，可以轻松与我畅谈各种数学界的奇闻轶事。'}
    hacker = {'role': Role.SYSTEM,
              'content': '你是一名高级黑客，你有着高超的代码编写能力，能指导我写各种脚本。'}
    teacher = {'role': Role.SYSTEM,
              'content': '你是一名高级讲师，我需要你为我进行语文功课辅导，你能掌握很多语文方面的修辞方法，能够知道汉语句子里面隐含的深层内容。'}
    data = Lawyer
    print("liuqidong",hashId,'system',data['content'])
    # //  忘记清空导致请求出错
    messages = list()
    commitValue("liuqidong",hashId,'system',data['content'])
# 转接到方法层的入口
def getResponse(name,queryId,query):
    return call_with_messages(name,queryId,query)
# 将用户的一条记录存入数据库
def commitValue(name,hashValue,dialogType,message):
    global messages
    newDict = {'role': dialogType, 'content': message}
    messages.append(newDict)
    # 提交事务
    db=linkMysql()
    # //  query为null时就是提示词
    sql= r"insert into template (userName,hashValue,dialogType,message) values ('{}','{}','{}','{}')".format(name,hashValue,dialogType,serialization(message))
    print("打印sql",sql)
    res = commitInfo(db,sql)
    print("执行结果",res)

def getValue(hashValue):
    db = linkMysql()
    sql  = r"SELECT * FROM `template` where hashValue = '{}'".format(hashValue)
    res =  commitInfo(db,sql)
    print("打印获取结果",res)
    return  res

def printDialog(message):
    print("+".join(['*' for i in range(20)]))
    for i in message:
        print(i)

# 通义千问开源模型：72b
def call_with_messages(name,queryId,query):
    global messages,hashId
    print("打印ID",queryId,1,queryId==1,)
    if (int(queryId) == 1):
        hashId = getTimeInteger()
        definePrompt()
    # 将用户的提问持久化
    commitValue(name,hashId, 'user',query)
    response = dashscope.Generation.call(
        MOUDLE_NAME,
        messages=messages,
        result_format='message',  # set the result is message format.
    )
    # print("输出，每轮信息",messages)
    printDialog(messages)
    if response.status_code == HTTPStatus.OK:
        print("请求成功，信息：{}".format(response))
        responseRole,responseContent = response.output.choices[0]['message']['role'],response.output.choices[0]['message']['content']
        commitValue(name,hashId,responseRole,responseContent)

        return [response.output.choices[0].message.content,hashId]
    else:
        print('Request id: {}, Status code: {}\n, error code: {}, error message: {}\n'.format(response.request_id, response.status_code,response.code, response.message))
        return ['出错了！事务提交失败！！！',0]

def getData(hashValue):
    import urllib.parse
    datas = getValue(hashValue)
    resList=list()
    dict1=dict()
    index = 1
    # 开始处理数据
    for i in datas:

        if i[3]=='user':
            dict1['hashValue'] = i[2]
            # dict1['query'] = urllib.parse.unquote(i[4])
            dict1['query'] = decode_unicode_sequences(i[4])
            dict1['id'] = index
            index = index+1
        elif (i[3]=='assistant'):
            # dict1['response'] = urllib.parse.quote(i[4])
            dict1['response'] = decode_unicode_sequences(i[4])
            resList.append(dict1)
            dict1=dict()
    print("打印dict1",resList)
    return resList