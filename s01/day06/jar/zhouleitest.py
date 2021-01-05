# def select_data(cls, username):
#     class_name = cls.__name__
#     user_dir_path = os.path.join(setting.DB_PATH, class_name)
#
#     if not os.path.exists(user_dir_path):
#         os.mkdir(user_dir_path)
#     user_path = os.path.join(user_dir_path, username)
#     if os.path.exists(user_path):
#         with open(user_path, mode='rb') as f:
#             obj = pickle.load(f)
#             return obj
#     else:
#         return None

if __name__ == '__main__':

    import os, sys
    import re

    sys.path.append(os.path.dirname(__file__))
    filePath = r'%s' % os.path.dirname(__file__)

    k_list = []
    for i, j, k in os.walk(filePath):
        k_list = k

    duplicate_list = []
    duplicate_full_list = []
    for item in k_list:
        if '.jar' in item:
            unit = re.findall(r'\D+\d+', item)
            test_list = item.split('-')
            temp_value = ''
            temp_list = {'unit1': None, 'number': None}
            flag2 = False
            for item in test_list:
                flag = item[0].isdigit()
                if not flag:
                    temp_value = temp_value + item + '-'
                else:
                    flag2 = True
                    temp_list['number'] = item
                    break
            temp_list['unit1'] = temp_value[0:len(temp_value) - 1]
            print(temp_list)

            duplicate_full_list.append(temp_list)
            if flag2:
                duplicate_list.append(temp_value[0:len(temp_value) - 1])
    jar_list = []
    print('duplicate_list====',duplicate_list)
    print('duplicate_full_list====', duplicate_full_list)
    temp = []
    for item in duplicate_list:

        temp_list = []
        tag = 0
        if not item in temp:
            temp.append(item)
            print('temp is', temp)
            for i in duplicate_full_list:

                if i['unit1'] == item and (i['number'] is not None):
                    l = i['unit1'] + '-' + i['number']
                    temp_list.append(l)
                    tag += 1
                    print('temp_list is %%%', temp_list)
        if tag > 1:
            jar_list.append(temp_list)
            print('jar_list is',jar_list)

    with open(filePath + r'\test.log', mode='wt', encoding='utf-8')  as f:
        f.write('start write file\n')
    with open(filePath + r'\test.log', mode='at', encoding='utf-8')  as f:

        for item in jar_list:
            print('============start=============')
            f.write('============start=============\n')
            item.sort()
            for i in item:
                print(i)
                f.write('%s' % i + '\n')
            print('============end=============\n')
            f.write('============end=============\n\r')

    for item in jar_list:

        item.sort()
        with open(filePath + r'\test.log', mode='at', encoding='utf-8')  as f:
            for i in range(len(item) - 1):
                print('rm -rf %s' % item[i])
                f.write('rm -rf %s' % item[i] + '\n')
