
#while 循环


n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n ,sum))


languages = ["C", "C++", "Perl", "Python" , "java"]
for x in languages:
    print(x)


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===")

print("break和continue语句及循环中的else子句")

for letter in "Runoob":
    if letter == 'n':
        break
    print(letter)
print("结束")



for letter in "Runoob":
    if letter == 'n':
        continue
    print(letter)
print("结束")



print("=============================================")

for i in range(10):
    print(i)

print("=============================================")
for i in range(5,9):
    print(i)

#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
print("也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):")

for i in range(0, 10, 3) :
    print(i)

print("===========================")

for i in range(-20 , -100 , -10):
    print(i)


#Python pass是空语句，是为了保持程序结构的完整性。
#pass 不做任何事情，一般用做占位语句，如下实例

for letter in "Runoob":
    if letter == 'o':
        pass
        print("执行pass")
    print("当前字母:" + letter)


print("-------------------------------------------------")

print("使用内置 enumerate 函数进行遍历:")
sequence = [12, 34, 34, 23, 45, 76, 89]
for i,j in enumerate(sequence):
    print(i,j)



print("循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。")

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0 :
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')




















