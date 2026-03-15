print("欢迎使用简易计算器！")

# 主循环：实现重复计算
while True:
    # 输入第一个数字
    num1 = float(input("请输入第一个数字："))
    # 输入第二个数字
    num2 = float(input("请输入第二个数字："))
    # 输入运算符
    op = input("请输入运算符号(+、-、*、/)：")
    
    # 输入校验：判断是否为合法运算符
    if op not in ["+", "-", "*", "/"]:
        print("请输入正确的运算符号")
    else:
        # 运算执行：根据运算符计算结果
        if op == "+":
            result = num1 + num2
            print(f"计算结果：{num1} + {num2} = {result}")
        elif op == "-":
            result = num1 - num2
            print(f"计算结果：{num1} - {num2} = {result}")
        elif op == "*":
            result = num1 * num2
            print(f"计算结果：{num1} * {num2} = {result}")
        elif op == "/":
            # 除数为0的特殊处理
            if num2 == 0:
                print("除数不能为 0")
            else:
                result = num1 / num2
                print(f"计算结果：{num1} / {num2} = {result}")
    
    # 询问是否继续
    again = input("是否继续计算？(y/n)：")
    if again.lower() != "y":
        print("感谢使用，再见！")
        break
