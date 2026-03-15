todo_list = []

# 菜单显示模块
def show_menu():
    print("\n===== 待办事项清单 =====")
    print("1. 添加待办")
    print("2. 查看所有待办")
    print("3. 删除指定待办")
    print("4. 退出")
    print("========================")

# 添加待办模块
def add_todo():
    content = input("请输入待办事项内容：")
    todo_list.append(content)
    print("添加成功！")

# 查看待办模块
def show_todos():
    if not todo_list:
        print("当前没有待办事项")
        return
    print("\n--- 待办事项列表 ---")
    for i, todo in enumerate(todo_list, 1):
        print(f"{i}. {todo}")

# 删除待办模块
def delete_todo():
    if not todo_list:
        print("当前没有待办事项")
        return
    show_todos()
    try:
        index = int(input("请输入要删除的待办序号："))
        if 1 <= index <= len(todo_list):
            deleted = todo_list.pop(index - 1)
            print(f"已删除：{deleted}")
        else:
            print("序号错误，请重新选择")
    except ValueError:
        print("请输入有效的数字")

# 主循环模块
while True:
    show_menu()
    choice = input("请输入操作序号：")
    
    if choice == "1":
        add_todo()
    elif choice == "2":
        show_todos()
    elif choice == "3":
        delete_todo()
    elif choice == "4":
        print("感谢使用，再见！")
        break
    else:
        print("输入错误，请重新选择")
