todo_list = []
while True:
    # 菜单显示
    print("\n===== 待办事项清单 =====")
    print("1.添加待办 2.查看所有待办 3.删除指定待办 4.退出")
    choice = input("请选择操作：")
    
    if choice == "1":
        # 添加待办
        todo = input("请输入待办事项：")
        todo_list.append(todo)
        print("添加成功！")
    elif choice == "2":
        if not todo_list:
            print("暂无待办事项")
        else:
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
    elif choice == "3":
        # 删除待办
        if not todo_list:
            print("暂无待办事项可删除")
            continue
        num = input("请输入要删除的序号：")
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(todo_list):
                del todo_list[idx]
                print("删除成功！")
            else:
                print("序号错误，请重新选择")
        else:
            print("请输入有效的数字！")
    elif choice == "4":
        print("程序已退出")
        break
    else:
        print("无效选择，请重新输入")
