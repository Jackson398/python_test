# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    if True:
        print("True")
    else:
        print("False")

    word = 'word'
    sentence = "这是一个句子。"
    paragraph = """这是一个段落。"""
    total = word + \
            sentence + \
            paragraph
    print(total)

    import sys;
    x = 'runoob';
    sys.stdout.write(x + '\n')  # Python可以在同一行中使用多条语句，语句之间使用分号(;)分割

    # print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
    x1 = "a"
    y1 = "b"
    # 换行输出
    print(x1)
    print(y1)

    print('---------')
    # 不换行输出
    print(x1, y1)

    # Python
    # 变量存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。
    #
    # 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
    #
    # 因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符
    # 中的变量赋值不需要类型声明。
    #
    # 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
    #
    # 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    #
    # 等号 = 用来给变量赋值。
    #
    # 等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值

    counter = 100  # 赋值整型变量
    miles = 1000.0  # 浮点型
    name = "John"  # 字符串

    print(counter)
    print(miles)
    print(name)

    # 同时为多个变量赋值
    a = b = c = 1
    print(a, b, c)

    # 两个整型对象1和2分别分配给变量a和b，字符串对象"john"分配给变量c
    a, b, c = 1, 2, "john"
    print(a, b, c)

    # 在内存中存储的数据可以有多种类型
    #
    # Python
    # 定义了一些标准类型，用于存储各种类型的数据
    #
    # Python有五个标准的数据类型：
    #
    # Numbers（数字）
    # String（字符串）
    # List（列表）
    # Tuple（元组）
    # Dictionary（字典）

    var1 = 1
    var2 = 10
    print(var1, var2)
    var1 = "12"  # 数字数据类型是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象
    print(var1)
    del var1, var2  # 通过使用del语句删除单个或多个对象的引用
    # print(var1, var2) UnboundLocalError: local variable 'var1' referenced before assignment

    # Python支持四种不同的数字类型：
    #
    # int（有符号整型）
    # long（长整型[也可以代表八进制和十六进制]）
    # float（浮点型）
    # complex（复数）

    # 如果你要实现从字符串中获取一段子字符串的话，可以使用[头下标:尾下标]
    # 来截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
    # [头下标: 尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符
    s1 = "abcdefghijklmn"
    s2 = s1[1:4]  # bcd
    s3 = s1[-8:-2]  # ghijkl
    s4 = s1[:]  # abcdefghijklmn
    print(s1, s2, s3, s4)

    # 加号（+）是字符串连接运算符，星号（ * ）是重复操作
    str1 = 'Hello World!'

    print(str1)  # 输出完整字符串 Hello World!
    print(str1[0])  # 输出字符串中的第一个字符 H
    print(str1[2:5])  # 输出字符串中第三个至第六个之间的字符串 llo
    print(str1[2:])  # 输出从第三个字符开始的字符串 llo World!
    print(str1 * 2)  # 输出字符串两次 Hello World!Hello World!
    print(str1 + "TEST")  # 输出连接的字符串 Hello World!TEST

    # 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引1到索引4的位置并设置为步长为2（间隔一个位置）来截取字符串
    letters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    letters2 = letters1[1:7:2]
    print(letters2)  # ['b', 'd', 'f']

    # 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）
    list1 = ['runoob', 786, 2.23, 'john', 70.2]
    tinylist1 = [123, 'john']

    print(list1)  # 输出完整列表 ['runoob', 786, 2.23, 'john', 70.2]
    print(list1[0])  # 输出列表的第一个元素 runoob
    print(list1[1:3])  # 输出第二个至第三个元素 [786, 2.23]
    print(list1[2:])  # 输出从第三个开始至列表末尾的所有元素 [2.23, 'john', 70.2]
    print(tinylist1 * 2)  # 输出列表两次 [123, 'john', 123, 'john']
    print(list1 + tinylist1)  # 打印组合的列表 ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

    tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
    tinytuple1 = (123, 'john')

    # 元组是另一个数据类型，类似于List（列表）。
    # 元组用()
    # 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
    print(tuple1)  # 输出完整元组 ('runoob', 786, 2.23, 'john', 70.2)
    print(tuple1[0])  # 输出元组的第一个元素 runoob
    print(tuple1[1:3])  # 输出第二个至第四个（不包含）的元素 (786, 2.23)
    print(tuple1[2:])  # 输出从第三个开始至列表末尾的所有元素 (2.23, 'john', 70.2)
    print(tinytuple1 * 2)  # 输出元组两次 (123, 'john', 123, 'john')
    print(tuple1 + tinytuple1)  # 打印组合的元组 ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

    # tuple1[2] = 1000  # 元组中是非法应用 TypeError: 'tuple' object does not support item assignment
    list1[2] = 1000  # 列表中是合法应用

    # 字典(dictionary)
    # 是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
    #
    # 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    #
    # 字典用"{ }"标识。字典由索引(key)和它对应的值value组成
    tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
    print(tinydict)  # 输出完整的字典 {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
    print(tinydict.keys())  # 输出所有键 dict_keys(['name', 'code', 'dept'])
    print(tinydict.values())  # 输出所有值 dict_values(['runoob', 6734, 'sales'])

    a = 10
    b = 3
    c = a ** b
    print("c=", c)  # 幂 1000

    # 取整除 - 返回商的整数部分（向下取整）
    c1 = 9 // 2
    print("c1=", c1)  # 4
    c2 = -9 // 2
    print("c2=", c2)  # -5

    # Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可
    print("1/2", 1 / 2)
    print("1.0/2", 1.0 / 2)
    print("1/float(2)", 1 / float(2))

    # Python数据类型转换
    # 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    #
    # 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值
    # https://www.runoob.com/python/python-variable-types.html

    # 缩进相同的一组语句构成一个代码块，我们称之代码组。
    #
    # 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
    #
    # 我们将首行及后面的代码组称为一个子句(clause)
    # if expression:
    #     suite
    # elif expression:
    #     suite
    # else:
    #     suite

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
