#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    cout << "欢迎来到数字猜谜游戏！" << endl;
    while (true) {
        int answer = rand() % 100 + 1, count = 0, g;
        cout << "\n我已经想好了一个1-100之间的数字，请开始猜吧！" << endl;
        while (true) {
            cout << "请输入你的猜测：";
            if (!(cin >> g)) {
                cout << "请输入有效的数字！" << endl;
                cin.clear();
                cin.ignore(1000, '\n');
                continue;
            }
            count++;
            if (g > answer) cout << "你猜的数字是 " << g << "，猜大了！" << endl;
            else if (g < answer) cout << "你猜的数字是 " << g << "，猜小了！" << endl;
            else {
                cout << "恭喜你猜对了！答案就是 " << answer << "，你共猜了 " << count << " 次。" << endl;
                break;
            }
        }
        char again;
        cout << "是否重新开始游戏？(y/n)：";
        cin >> again;
        if (again != 'y' && again != 'Y') {
            cout << "感谢游玩，再见！" << endl;
            break;
        }
    }
    return 0;
}
