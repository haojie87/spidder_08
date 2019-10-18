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

```
sudo pip3 install pyexecjs
sudo pip3 install nodejs
```

