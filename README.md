# wxcloudrun-django
微信云托管 django 框架模版


## 简介
了解在微信云托管上如何用python的django框架创建简单的http服务。通过示例创建一张todo_list表，并对其进行增删改查的操作，对应POST/DELETE/PUT/GET四种请求的实现。
Django (https://www.djangoproject.com/) 是一个开源的Web应用框架，由Python写成，鼓励简洁实用的设计和敏捷快速的开发方式。

## 详细介绍

1. 本示例中，使用的是django 3.2.7，通过80端口对外。
   * 如需修改端口号，请到Dockerfile中修改。
   * 修改端口号之后，如果使用流水线部署版本，请确保container.config.json中的containerPort字段也同步修改；如果在微信云托管控制台手动「新建版本」，请确保“监听端口”字段与代码中端口号保持一致，否则会引发部署失败。
2. 在微信云托管控制台一键部署本示例，会同时自动开通环境内的MySQL服务并完成初始化，后续可直接使用。数据库的地址、帐号、密码会被作为环境变量默认注入，settings.py中直接引用。
   * 如不想使用微信云托管自带的MySQL，请手动修改settings.py中数据库信息并在微信云托管控制台注销MySQL。
   * 未通过一键部署按钮，而是直接使用本示例的代表进行部署，需要手动在微信云托管控制台中开通MySQL，且数据库信息不会默认注入。在新建版本时需要手动将数据库信息作为环境变量填入。
3. 基于示例二次开发操作步骤：
   * 在微信云托管控制台一键部署，完成服务创建、MySQL初始化、首个版本部署上线。
   * fork示例代码到自己的代码仓库，在此基础上进行二次开发。
   * 服务的第二个及后续版本，基于自己的代码仓库进行部署。
4. 代码仓库中的container.config.json文件仅用于在微信云托管中创建流水线。如果不使用流水线，而是用本项目的代码在微信云托管控制台手动「新建版本」，则container.config.json配置文件不生效。最终版本部署效果以「新建版本」窗口中手动填写的值为准。

## 目录结构

~~~
.
├── Dockerfile                  dockerfile
├── README.md                   README.md文件
├── container.config.json       微信云托管流水线配置
├── manage.py                   django项目管理文件 与项目进行交互的命令行工具集的入口
├── requirements.txt            依赖包文件
└── wxcloudrun                  app目录
    ├── __init__.py             python项目必带  模块化思想
    ├── apps.py                 自动生成文件apps.py
    ├── asgi.py                 自动生成文件asgi.py, 异步服务网关接口
    ├── migrations              数据移植（迁移）模块
    ├── models.py               数据模块
    ├── settings.py             项目的总配置文件  里面包含数据库 web应用 日志等各种配置
    ├── templates               模版目录,包含主页index.html文件
    ├── urls.py                 URL配置文件  Django项目中所有地址中（页面）都需要我们自己去配置其URL
    ├── views.py                执行响应的代码所在模块  代码逻辑处理主要地点  项目大部分代码在此编写
    └── wsgi.py                 自动生成文件wsgi.py, Web服务网关接口
~~~

## 示例API列表

1 查询所有todo项

* URL路径：
  ```/api/todos```
  
* 请求示例：
```
curl -X GET  http://{ip}:{port}/api/todos
```

* 响应示例：
```
{
  "code": 0,
  "errorMsg": "",
  "data": [{
    "id": 1,
    "title": "工作1",
    "status": "准备中",
    "create_time": "2021-11-09T08:45:40Z",
    "update_time": "2021-11-09T08:45:40Z"
  }, {
    "id": 2,
    "title": "工作2",
    "status": "已开始",
    "create_time": "2021-11-09T08:46:11Z",
    "update_time": "2021-11-09T08:46:11Z"
  }]
}
```


2 根据ID查询todo项

* URL路径：
  ```/api/todos/:id```
  
* 请求示例：
```
curl -X GET  http://{ip}:{port}/api/todos/1
```

* 响应示例：
```
{
  "code": 0,
  "errorMsg": "",
  "data": {
    "id": 1,
    "title": "工作1",
    "status": "准备中",
    "create_time": "2021-11-09T08:45:40Z",
    "update_time": "2021-11-09T08:45:40Z"
  }
}
```


3 新增todo项目

* URL路径：
  ```/api/todos```
  
* 请求示例：
```
curl http://{ip}:{port}/api/todos \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{  
    "title":"工作1",
    "status":"准备中"
  }'
```

* 响应示例：
```
{
  "code": 0,
  "errorMsg": "",
  "data": {
    "id": 1,
    "title": "工作1",
    "status": "准备中",
    "create_time": "2021-11-09T08:45:40Z",
    "update_time": "2021-11-09T08:45:40Z"
  }
}
```

4 根据ID修改todo项目

* URL路径：
  ```/api/todos```
  
* 请求示例：
```
curl http://{ip}:{port}/api/todos \
  -X PUT \
  -H 'Content-Type: application/json' \
  -d '{  
    "id":1,
    "status":"已完成"
  }'
```

* 响应示例：
```
{
  "code": 0,
  "errorMsg": ""
}
```

5 根据ID删除todo项

* URL路径：
  ```/api/todos/:id```
  
* 请求示例：
```
curl http://{ip}:{port}/api/todos/1 \
  -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{   }'
```

* 响应示例：
```
{
  "code": 0,
  "errorMsg": ""
}
```

