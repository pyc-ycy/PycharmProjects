#!/usr/bin/python3.7
#-*-coding:UTF-8-*-
#if的用法：

#name = input("name:")
#age = input("age:")
#job = input("job:")
#salary = input("salary:")

'''info = --------info of %s-------
name:%s
age:%s
job:%s
salary:%s
--------------------------------------''' #% (name, name, age, job, salary)
'''print(info)

info2 = --------info of {_name}-------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
--------------------------------------'''#.format(_name=name, _age=age, _job=job, _salary=salary)
#print(info2


person = ["name", ["saving", 1000]]

p1 = person[:]
p2 = person[:]
p1[0] = "Alex"
p2[0] = "Jenny"
p1[1][1] = 500
print(p1)
print(p2)


