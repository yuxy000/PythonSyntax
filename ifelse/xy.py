import random

x = random.choice(range(100))
y = random.choice(range(200))

if x > y:
    print("x:", x)
elif x == y:
    print("x + y:", x + y)
else:
    print("y:", y)


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


height = 1.75
weight = 40.5
name = '小米'
bmi = weight / height ** 2
if bmi < 18.5:
    print("%s 的BMI指数是 %.1f, 体重过轻" % (name, bmi))
elif bmi <= 25:
    print("%s 的BMI指数是 %.1f, 体重正常" % (name, bmi))
elif bmi <= 28:
    print("%s 的BMI指数是 %.1f, 体重过重" % (name, bmi))
elif bmi <= 32:
    print("%s 的BMI指数是 %.1f, 肥胖" % (name, bmi))
else:
    print("%s 的BMI指数是 %.1f, 严重肥胖" % (name, bmi))
