import os

# 指定目录路径
directory = r"C:\Users\seana\OneDrive\文件 1"

# 获取目录中的文件列表
file_list = os.listdir(directory)

# 打印文件列表
for file_name in file_list:
    print(file_name)
