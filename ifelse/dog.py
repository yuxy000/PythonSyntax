print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入你家狗的年龄："))
        print("")
        if age < 0:
            print("你在逗我吧")
            break
        elif age == 1:
            print("相当于 14 岁的人")
            break
        elif age == 2:
            print("相当于 22 岁的人。")
            break
        elif age > 2:
            human = 22 + (age - 2)*5
            print("对应人类年龄: ", human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")

# 退出提示
input("点击 enter 键退出")
