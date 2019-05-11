#!/usr/bin/env python3.7
# -*-coding:UTF-8-*-
'''true_age = 20
count = 0
while count<3:
   guess_age = int(input("输入年龄："))
   if guess_age == true_age:
       print("Yes,you got it!")
       break
   elif guess_age > true_age:
       print("think smaller")
   else:
       print("think bigger")
   count +=1
   if count ==3:
       continue_comfirm = input("do you want to keep guessing...")
       if continue_comfirm != "no":
            count = 0
print("-----------------")
n =1
while n < 10:
    print("当前的数字：",n)
    n += 1
print(" ")
print("----for 循环------")
for k in 'Good123':
    print("输出字符：",k)
print("------------------")
tups = {"name":"Toney","job":"Accountant"}
for key,value in tups.items():
	print("%s:%s"%(key,value))

for i in range(0,20,2):
    print(i)'''


def quicksort(x):
    qsort(x, 0, len(x) - 1)
    return


def qsort(x, first, last):
    if first < last:
        split = partition(x, first, last)
        qsort(x, first, split - 1)
        qsort(x, split + 1, last)
    return


def partition(x, first, last):
    pivot = x[first]  # 选取列表中的第一个元素作为划分元素
    leftmark = first + 1
    rightmark = last
    while True:  # 如果列表中存在与划分元素pivot相等的元素，让它位于left部分
        while x[leftmark] <= pivot:  # 检测pivot是否是列表中最大的元素
            if leftmark == rightmark:
                break  # 防止leftmark越界
            leftmark += 1
        while x[rightmark] > pivot:
            rightmark -= 1
        if leftmark < rightmark:
            x[leftmark], x[rightmark] = x[rightmark], x[leftmark]
        else:
            break
    x[first], x[rightmark] = x[rightmark], x[first]
    return rightmark  # 返回pivot的最终位置


num_list = [5, -4, 6, 3, 7, 11, 12]
print(len(num_list))
print("排序之前：" + str(num_list))
quicksort(num_list)
print("排序之后：" + str(num_list))


def func(str_):
    dict_char_tmp = {i: str_.count(i) for i in str_}  # 得到所有单词的个数
    print('得到所有单词的个数:', dict_char_tmp)
    dict_char = {}
    for k, v in dict_char_tmp.items():
        if dict_char.get(v):
            dict_char[v].append(k)
        else:
            dict_char[v] = [k]
    # print dict_char
    dict_char_k = sorted(dict_char.items(), key=lambda item: item[1], reverse=True)
    print(dict_char_k)
    char_l = dict_char_k[0][1]
    char_l.sort()
    print('得到出现次数最多的字母：', char_l[0], ',个数是：', dict_char_k[0][0])


a = 'hellow'
func(a)


def fun(x):
    y = list(x)
    c = []
    for i in range(0, len(y)):
        print(y[i], ":", y.count(y[i]))
        z = y.count(y[i])
        c.append(z)
    # print(max(c))
    # print(c)
    for j in range(0, len(y)):
        if y.count(y[j]) == max(c):
            print(y[j])



