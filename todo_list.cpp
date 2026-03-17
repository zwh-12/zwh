#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> todos;

// 添加待办
void addTodo() {
    string todo;
    cout << "请输入待办事项：";
    cin.ignore();
    getline(cin, todo);
    todos.push_back(todo);
    cout << "添加成功！" << endl;
}

// 查看待办
void showTodos() {
    if (todos.empty()) {
        cout << "暂无待办事项" << endl;
        return;
    }
    for (int i = 0; i < todos.size(); i++) {
        cout << i + 1 << ". " << todos[i] << endl;
    }
}

// 删除待办
void deleteTodo() {
    if (todos.empty()) {
        cout << "暂无待办事项可删除" << endl;
        return;
    }
    int num;
    cout << "请输入要删除的序号：";
    if (!(cin >> num) || num < 1 || num > todos.size()) {
        cout << "序号错误，请重新输入" << endl;
        cin.clear();
        cin.ignore(1000, '\n');
        return;
    }
    todos.erase(todos.begin() + num - 1);
    cout << "删除成功！" << endl;
}

int main() {
    int choice;
    while (true) {
        // 菜单显示
        cout << "\n===== 待办事项清单 =====" << endl;
        cout << "1.添加待办 2.查看所有待办 3.删除指定待办 4.退出" << endl;
        cout << "请选择操作：";
        if (!(cin >> choice)) {
            cout << "无效选择，请重新输入" << endl;
            cin.clear();
            cin.ignore(1000, '\n');
            continue;
        }
        switch (choice) {
            case 1: addTodo(); break;
            case 2: showTodos(); break;
            case 3: deleteTodo(); break;
            case 4: cout << "程序已退出" << endl; return 0;
            default: cout << "无效选择，请重新输入" << endl;
        }
    }
}
