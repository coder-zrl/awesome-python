import os
def get_all_path(directory):
    rootdir = directory
    path_list = []
    list1 = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    # print(list1)
    for i in range(len(list1)):
        com_path = os.path.join(rootdir, list1[i])
        # print(com_path)
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    # print(path_list)
    return path_list
print(get_all_path('./'))