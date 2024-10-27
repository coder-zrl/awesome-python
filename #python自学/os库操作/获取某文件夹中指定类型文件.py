import os
path1=r'./'
for root, dirs, files in os.walk(path1):
    print(root)
    print(dirs)
    print(files)
    print('11111')
    for file in files:
        if file.endswith('.py'):
            print(os.path.join(root,file))
    print('2222')