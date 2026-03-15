55import random

print("欢迎来到数字猜谜游戏！")

# 主游戏循环
while True:
    # 生成谜底
    answer = random.randint(1, 100)
    count = 0
    
    print("\n我已经想好了一个1-100之间的数字，请开始猜吧！")
    
    # 猜测循环
    while True:
        guess = input("请输入你的猜测：")
        
        # 非数字输入处理
        if not guess.isdigit():
            print("请输入有效的数字！")
            continue
        
        guess = int(guess)
        count += 1
        
        # 判断结果
        if guess > answer:
            print(f"你猜的数字是 {guess}，猜大了！")
        elif guess < answer:
            print(f"你猜的数字是 {guess}，猜小了！")
        else:
            print(f"恭喜你猜对了！答案就是 {answer}，你共猜了 {count} 次。")
            break
    
    # 询问是否重新开始
    again = input("是否重新开始游戏？(y/n)：")
    if again.lower() != "y":
        print("感谢游玩，再见！")
        break
