#print('适合中文的str')
#将字符转换为整数表示
#print(ord('浮'))

#将编码转换为对应的字符
#print(chr(28014))

#encode函数：str通过encode（）函数可以编码为指定的bytes
#print('ABC'.encode('ascii'))
#print('浮'.encode('UTF-8'))
#print('浮'.encode('ascii')) #中文无法通过ASCII编码，因为超过了ASCII最大长度

#decode函数：通过decode（）函数将字节流解码
#print(b'\xe6\xb5\xae'.decode('utf-8'))
#print(b'\xe6\xb5\xae'.decode('utf-8'))

#len函数：计算str的字符数，如果换成byte，则会计算字节数；英文数字通常被算为1个字节，中文被算作3个字节
#print(len('ABC'))
#print(len('中文'))
#print(len(b'\xe4\xb5\xae'.decode('utf-8')))

#为了避免乱码问题，应始终坚持使用utf-8.所以一般需在写源代码之前加上以下内容,否则Python默认使用ascii编码
#!/usr/bin/env python3.9
#-*- coding: utf-8 -*-

#%运算符：用来格式化字符串，在字符串内部，%s表示字符串，%d表示整数，%f表示浮点数，有几个占位符，后面就跟几个变量，如果只有一个变量，可以不加括号
#print('Hello,%s' % '浮大猛')
#print('Hello,%s先生，您的话费余额为%.2f元，请于%d月%d日前补充话费' % ('浮增光',50.98123,3,12)) #%.2f用来控制浮点数小数点位数
#如果内容中有%，需要进行转移，用%%表达
#print('hello,%s先生，您的工作完成度还有%d%%尚未完成' % ('浮增光',30))

#fromat()格式化字符串：使用fromat（）方法，他会用传入的参数依次替换字符串内的{0},{1},{2}...
#print('{0}同学，你的本学期成绩为{1:.1f}'.format('小明',123.345))    #{1:.2f}来控制浮点数小数点位数，1表示第几个变量，2表示小数点后有几位

#LIST
#inpatient = ['刘礼畅','徐刘星悦','浮增光']  #list是一种有序集合，从0开始计数，可增加和删除集合内的值
'''if len(inpatient) >= 4:
    print(inpatient)
else:
    inpatient.append('测试数据')
    print(inpatient)'''
#append()函数：在集合尾增加值
'''inpatient.append('吴倩')
print(inpatient)'''
#insert()函数：在指定位置插入值
'''inpatient.insert(1,'吴倩')    #1表示在第几个位置插入值，后面跟插入的值
print(inpatient)'''
#pop(i)函数，删除指定位置的值
'''inpatient.pop(0)    #pop(i)i为空时，默认删除末尾值，i为整数时，删除对应位置的值
print(inpatient)'''
#直接赋值：inpatient[i]='str'    在集合指定位置替换值
'''inpatient[2] = '吴倩'
print(inpatient)'''

#二维数组:s = ['a','b','c',['d','e'],f]
'''s = ['a','b','c',['d','e'],'f']
print(len(s))'''
'''p = ['d','e']
s = ['a','b','c',p,'f']
print(s[3][0])'''   #如果想取二维数组中的值，语法为：一数组([对应二维数组位置][想取的值的位置])

#tuple元组
#tuple初始化后不可修改，在tuple中的list，可以修改list中的值，但是list不能变
'''t = (1,)
print(t)''' #当只有一个元素时，必须加一个都好来消除歧义，不加逗号则是将元素赋予变量

#if...elif...elif...else    #if语句执行特点：自上而下判断，如果在某个判断的结果为True，那么就执行当前的判断，忽略下面的判断
#age = [1,2,3]
'''if age >= 18:
    print('成年人')
elif age >= 6:
    print('青年')
else:
    print('儿童')'''

'''if age:
    print(age)'''   #if语句简写，只要变量为非零数值，非空字符串，非空list，就判断为True，否则判断为False

'''a = input('birth:')  
birth = int(a)
if birth > 2000:
    print('00后')
else:
    print('00前')''' #int将a的值从input的str转换为整数类型

'''a = input()  #这里为错误语法，因为input()返回的数据类型为string，所以，输入值之后，a被赋予值的类型为str，无法与2000比较，所以错误
if a > 2000:
    print('00后')
else:
    print('00前')'''

#练习：
#height = input('身高: ')
#weight = input('体重: ')
'''h = float(input('身高(米)：'))
w = float(input('体重（KG）： '))
BMI = w/(h*h)
if BMI >= 32:
    print('严重肥胖')
elif BMI >= 28:
    print('肥胖')
elif BMI >= 25:
    print('过重')
elif BMI >= 18.5:
    print('正常')
else:
    print('过轻')'''

#循环
#for x in ...循环：把每个元素依次代入x，然后执行缩进块内的语句
'''A = ['a','b','c']
for B in A:
    print(B)'''

'''A = 0
for B in [1,2,3,4]:
    A = A + B
print(A)'''

#range()函数：生成一个整数数列
#list(range())转换为list，将值依次填入
'''print(range(5))
print(list(range(5)))'''

#练习：
'''A = 0
for B in list(range(101)):
    A = A + B
print(A)'''

'''A = 0
B = 100
while B > 0:
    A = A + B
    B = B - 2
print(A)''' #while语句：条件满足时，不断循环；条件不满足时，退出循环

'''L = ['Bart','Lisa','Adam']
for A in L:
    print('Hello,',A)'''

#break:可以提前推出循环
'''n = 1
while n <= 100:
    print(n)
    n = n + 1
print('End')'''

'''n = 1
while n <= 100:
    if n > 10:  #当n=11时，满足>10的条件
        break   #break结束循环
    print(n)
    n = n + 1
print('End')'''

#continue：跳过当前循环，进入下一循环
'''n = 0
while n < 10:
    #n = n + 1
    if n % 2 == 0:
        continue
    print(n)'''

r = 4
area = r**2
circle = r**3
print('周长是''%s''cm²' % area)
print('面积是''%s''cm³'% circle)
