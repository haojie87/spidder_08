###### SQL命令

```python
# 1. 查询所有省市县信息（（连接查询实现）
select province.p_name,city.c_name,county.x_name from province inner join city on province.p_code=city.c_father_code inner join county on city.c_code=county.x_father_code;
# 2. 查询所有省市县信息（多表查询实现）
select province.p_name,city.c_name,county.x_name from province,city,county  where  province.p_code=city.c_father_code and  city.c_code=county.x_father_code;
```

###### 三个池子

```python
1、User-Agent池
2、代理IP池
3、cookie池
```

###### 安装pyexecjs模块

```python
# 将代码写入本地js文件,利用pyexecjs模块执行js代码进行调试
sudo pip3 install pyexecjs
```

###### 安装nodejs模块

```python
sudo pip3 install nodejs
```

###### scrapy框架

```python
# Ubuntu安装
1、安装依赖包
	1、sudo apt-get install libffi-dev
	2、sudo apt-get install libssl-dev
	3、sudo apt-get install libxml2-dev
	4、sudo apt-get install python3-dev
	5、sudo apt-get install libxslt1-dev
	6、sudo apt-get install zlib1g-dev
	7、sudo pip3 install -I -U service_identity
2、安装scrapy框架
	1、sudo pip3 install Scrapy
```

```python
# Windows安装
cmd命令行(管理员): python -m pip install Scrapy
# Error: Microsoft Visual C++ 14.0 is required xxx
```