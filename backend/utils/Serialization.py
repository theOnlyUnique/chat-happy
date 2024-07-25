import json

# 序列化为字符串
def serialization(obj):
    return json.dumps(obj)

# 反序列化为字符串
def reSerialization(str):
    return json.loads(str)