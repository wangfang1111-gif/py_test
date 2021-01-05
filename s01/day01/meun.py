# author:wang fang
# 三级菜单，依次选择进入各子菜单，列表，字典
maps = {'hunan':{'changsha':['kaifu', 'yuelu'],
                 'zhuzhou':['hehua', 'hetang']},
        'hubei': {'wuhan':['qiaodong', 'qiaoxi'],
                  'huanggang': ['gangdong', 'gangxi']},
        'guangdong': {'zhangzhou': ['tanan', 'taxi'],
                      'shantou': ['tou1', 'tou2']}}

while True:
    for i in maps:
        print(i)
    choice = input("选择进入：")
    if choice in maps:
        while True:
            for i2 in maps[choice]:
                print('\t\t',i2)
            choice2 = input("选择进入2：")
            if choice2 in maps[choice]:
                while True:
                    for i3 in maps[choice][choice2]:
                        print('\t\t', i3)
                    choice3 = input("选择进入3：")
                    if choice3 in maps[choice][choice2]:
                            for i4 in maps[choice][choice2]:
                                print('\t\t', choice3)








