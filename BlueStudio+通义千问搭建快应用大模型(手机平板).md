# BlueStudio+通义千问搭建快应用大模型(手机/平板)

# 零、环境说明

IDE：BlueStudio比赛版(前端)，Pycharm2023.1.4专业版（后端）

nvm:1.1.10

node:16.13.1

指导文档地址：[【赛题二】蓝河创新应用开发（手机、平板方向）开发手册 (qq.com)](https://docs.qq.com/doc/DV1puYmxmVnVWcmFs)

# 一、构建项目

## 1.1通义千问api-key申请

创建通义千问Api-key:[如何开通DashScope并创建API-KEY_模型服务灵积(DashScope)-阿里云帮助中心 (aliyun.com)](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key)

## 1.2后端构建

### （1）拉取项目

下载压缩包地址：https://h5.vivo.com.cn/blueos-atom/guidelines-phone/blueos-ai-app.zip

这样将获得前端和后端的源码

后端代码直接添加`api-key`和`host`运行即可

### （2）安装依赖

```
pip install -r ./requirement.txt
```

### （3）配置跨域和host

引入库

```python
# 配置跨域允许
from flask_cors import CORS # 添加这行导入
```

启用跨域支持(全局添加)

```
CORS(app,supports_credentials=True) # 添加这行，启用CORS支持
# supports_credentials是设置allow-cros
```

修改服务地址

```
app.run(host='10.6.3.226', port='6432')
# 注意替换为你实际的IP和PORT
```

配置文件

```python
from http import HTTPStatus
from flask import Flask, request
import dashscope
# 配置跨域允许
from flask_cors import CORS # 添加这行导入

# 首先注册通义千问账号，获得 DASHSCOPE_API_KEY
# 替换下方的 api_key
# 参考：https://help.aliyun.com/zh/dashscope/developer-reference/tongyi-qianwen-7b-14b-72b-quick-start?spm=a2c4g.11186623.0.0.18159b6eCAijjm

dashscope.api_key = 'sk-858b08878edd49b5b85fba03689be0fd' # 替换为你自己的 DASHSCOPE_API_KEY

print("执行main")
app = Flask(__name__)
CORS(app,supports_credentials=True) # 添加这行，启用CORS支持
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
    print("执行main")
    app.run(host='10.6.3.226', port='6432') # host 换成你自己的本地 ip。另外 frontend 蓝河应用代码中 getResponse 方法也要对应替换成自己的 ip
```

### （4）运行服务

在IDE直接运行即可



## 1.3前端构建

### （1）拉取项目

下载压缩包地址：https://h5.vivo.com.cn/blueos-atom/guidelines-phone/blueos-ai-app.zip

解压缩里面的front目录即可

### （2）安装依赖

```
pnpm i
```

### （3）修改访问地址

1.修改jsconfig.json的地址

2.修改index.js的地址

3.修改index.js.map的地址

4.修改index.ux的地址

### （4）本地演示

没有问题的话，控制台输出就是这样的

![](https://ikun-1322198038.cos.ap-guangzhou.myqcloud.com/undefined202403122157413.png)

## 1.3ADB(Android调试桥)搭建

### （1）下载地址

https://dl.google.com/android/repository/platform-tools-latest-windows.zip

### （2）安装手册

[如何在 Windows、MacOS 上安装 adb · Issue #120 · quickappcn/issues (github.com)](https://github.com/quickappcn/issues/issues/120)

### （3）启动adb

本文档演示在windows下的操作过程。

唤出cmd，输入如下指令

```
adb devices
```

然后在手机中基本可以看见`启用USB调试`的弹窗了

### （4）配置环境变量

这时候可能启动`BluseOS Studio`之后还是显示未找到`adb`指令，这时候需要我们去将我们安装的cdb的根目录添加到用户的环境变量里面去

以上步骤完成之后我们在`BluseOS Studio`里面启动adb调试，连接好数据线就可以自动下载快应用手机APP了（一共有两个）



## 1.4云真机使用教程



# 二、目前进度

## 2.1前端展现

对话过程展示

![](https://ikun-1322198038.cos.ap-guangzhou.myqcloud.com/undefined202403081928794.png)

## 2.2后端服务

![](https://ikun-1322198038.cos.ap-guangzhou.myqcloud.com/undefined202403081930475.png)



# 三、近期拓展目标

## 3.1云上部署[√]

​		将项目部署到远程云端服务器，提供线上演示

## 3.1前端交互拓展

## （1）个性化主题定制[√]

​		包括基础的白天、黑夜模式，以及系统预设的其他主题模板。

​		部分精美主题能提供些许特效，当用户绑定账户后使用可以购买自己喜爱的主题



## （2）文本联想

​		当用户输入提问语句时，后台可以使用流处理等相关技术来联想一些关键词，一来能够吸引用户的注意力，节省用户输入的时间，二来能够增强用户粘性。

​		如果接入网络联想当下热门事件，并撰写评论文章、总结事件发生流程，预计能收获不错的流量



## （3）生词跳转

当出现比较生僻的单词的时候，生成悬浮卡片，用户鼠标上浮即可查看词条，在移动端点击即可查看词条



## 3.2后端服务拓展

## （1）情感语义优化

​		大模型作为一种AIGC(生成式人工智能)，能够理解人们的提问，并根据内部训练数据生成回答。

​		可以通过分析提问者的情绪来相应地输出对应地带有情绪价值的语句，举一个极端的例子

​		比如当用户遭受到到重大打击时，用户可能不会那么细致地描述自己的遭遇，而是会输入一些带有强烈情感色彩的简短语句，这是我们需要输出带有情绪价值的回复来安慰使用者，而不是给出一些客观的建议。

​		后端可以对用户输入的文本的情感进行评估，然后根据用户情感强烈程度给出相应的回复

![](https://ikun-1322198038.cos.ap-guangzhou.myqcloud.com/undefined202403081905197.png)



## （2）文本/文件处理

​		支持用户通过特定的入口上传文件，能够根据用户上传的文件类型提供对应功能。比如用户上传文本，可以总结出文本的信息；用户上传excel，可以对excel的数据进行部分操作；用户指定语言上传一段代码块，能够解析代码每一步的含义



## （3）预设模板[√]

​		用户可以给出一段prompt（训练提示词）来初始化一个将要对话的GPT，GPT将全局围绕这段prompt来进行回答



## （4）摇一摇匹配他人模板

​		利用手机传感器与用户进行互动，用户可以通过摇一摇随机匹配他人训练的GPT模板进行互动。用户也可以将自己训练的模板通过链接的形式分享给好友导入使用。

## （5）连续对话[√]



# 四、项目评测

见演示视频



# 五、参考



