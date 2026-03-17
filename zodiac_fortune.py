zodiac_ranges = [
    # 水瓶座:1月20日-2月18日, 双鱼座:2月19日-3月20日, 白羊座:3月21日-4月19日
    (120, 218, "水瓶座"), (219, 320, "双鱼座"), (321, 419, "白羊座"),
    # 金牛座:4月20日-5月20日, 双子座:5月21日-6月21日, 巨蟹座:6月22日-7月22日
    (420, 520, "金牛座"), (521, 621, "双子座"), (622, 722, "巨蟹座"),
    # 狮子座:7月23日-8月22日, 处女座:8月23日-9月22日, 天秤座:9月23日-10月23日
    (723, 822, "狮子座"), (823, 922, "处女座"), (923, 1023, "天秤座"),
    # 天蝎座:10月24日-11月22日, 射手座:11月23日-12月21日, 摩羯座:12月22日-1月19日
    (1024, 1122, "天蝎座"), (1123, 1221, "射手座")
]

zodiac_fortunes = {
    "白羊座": "今日运势：财运上升，注意休息",
    "金牛座": "今日运势：工作顺利，适合理财",
    "双子座": "今日运势：社交活跃，注意沟通",
    "巨蟹座": "今日运势：家庭和睦，注意情绪",
    "狮子座": "今日运势：自信满满，适合表现",
    "处女座": "今日运势：细心谨慎，工作高效",
    "天秤座": "今日运势：运势平稳，注意选择",
    "天蝎座": "今日运势：洞察力强，适合决策",
    "射手座": "今日运势：精力充沛，适合外出",
    "摩羯座": "今日运势：务实稳重，注意健康",
    "水瓶座": "今日运势：创意丰富，适合创新",
    "双鱼座": "今日运势：灵感涌现，注意休息"
}

def get_zodiac(month, day):
    date_num = month * 100 + day
    if date_num >= 1222 or date_num <= 119:
        return "摩羯座"
    for start, end, name in zodiac_ranges:
        if start <= date_num <= end:
            return name
    return None

def is_valid_date(month, day):
    if month < 1 or month > 12:
        return False
    max_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    return 1 <= day <= max_days[month-1]

while True:
    birthday = input("\n请输入生日（格式：月-日，如 3-21）：")
    parts = birthday.split("-")
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        print("生日格式错误，请输入 月-日（如 3-21）")
        continue
    
    month, day = int(parts[0]), int(parts[1])
    if not is_valid_date(month, day):
        print("生日格式错误，请输入 月-日（如 3-21）")
        continue
    
    zodiac = get_zodiac(month, day)
    print(f"你的星座是{zodiac}，{zodiac_fortunes[zodiac]}")
    
    while True:
        again = input("是否继续查询？(y/n)：").lower()
        if again == "y":
            break
        elif again == "n":
            print("程序已退出")
            break
        else:
            print("请输入 y 或 n")
    if again == "n":
        break
