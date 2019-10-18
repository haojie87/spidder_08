import execjs

with open('translate.js','r') as f:
    data=f.read()

# 1.创建一个编译对象
jsobj = execjs.compile(data)
sign = jsobj.eval('e("tiger")')

print(sign)
