/data 存放请求数据与配置信息和默认参数

/function 存放相对应的函数 以供调用

/test  进行单元测试的模块

/requirement.txt 项目所需依赖
```
pip install -r ./requirement.txt
```

/server.py  项目主目录，再次运行项目提供服务



| Code | Status                     | 可能的原因                                                   | 含义说明                         |
| ---- | -------------------------- | ------------------------------------------------------------ | -------------------------------- |
| 400  | InvalidParameter           | Required parameter(s) missing or invalid, please check the request parameters.(可根据实际情况修改) | 接口调用参数不合法               |
| 429  | Throttling                 | Requests throttling triggered.                               | 接口调用触发限流                 |
| 429  | Throttling.RateQuota       | Requests rate limit exceeded, please try again later.        | 调用频次触发限流，比如 QPM       |
| 429  | Throttling.AllocationQuota | Allocated quota exceeded, please increase your quota limit.  | 一段时间调用量触发限流，比如 TPM |
| 500  | InternalError              | An internal error has occured, please try again later or contact service support.(可根据实际情况修改) | 内部错误                         |
| 500  | InternalError.Algo         | An internal error has occured during execution, please try again later or contact service support.(可根据实际情况修改) | 内部算法错误                     |

