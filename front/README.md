# 快应用示例模版

## 文件结构

```
└── src
│   ├── assets          # 公用的资源(images/styles/字体...)
│   │   ├──images       # 存储 png/jpg/svg 等公共图片资源
│   │   └──styles       # 存放 less/css/sass 等公共样式资源
│   │   └──js           # 存储公共 javaScript 代码资源
│   │   └──iconfont     # 存放图标字体文件
│   ├── helper          # 项目自定义辅助各类工具
│   │   ├──ajax.js      # 对系统提供的 fetch api 进行链式封装
│   │   └──utils        # 存放项目所封装的工具类方法
│   ├── pages           # 统一存放项目页面级代码目录
│   ├── app.ux          # 应用程序代码的入口
│   ├── manifest.json   # 配置应用基本信息
│   └── components      # 存放应用公共组件
└── package.json        # 定义项目需要的各种模块及配置信息
```

### 模版说明

- `Demo` 页面：示例页面；
- `DemoDetail`页面：详情页面；

## 模版介绍

- **更优雅的处理数据请求**；采用 `Promise` 对系统内置请求 `@system.fetch` 进行封装，并抛出至全局，使得可以极简的进行链式调用，并能够使用 `finally`；
- **内置样式处理方案**；「快应用」支持 `less`, `sass` 的预编译；这里采取 [dart sass](https://sass-lang.com/documentation) 方案，并内置了部分变量，以及常用混合方法，使得可以轻松开启样式编写、复用、修改等；
- **添加新增页面命令脚本**；如果需要新建页面，只需运行：`yarn gen YourPageName` ，当然，也可以根据需要，自行定定制模板：_/command/gen/template.ux_；
- 集成 [Prettier](https://prettier.io/)；在检测代码中潜在问题的同时，统一团队代码规范、风格（`js`，`less`，`scss`等），从而促使写出高质量代码，以提升工作效率(尤其针对团队开发)；

# node版本