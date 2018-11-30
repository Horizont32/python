import os

# Open a file
path = "D:/YandexDisk/СделатьЛехе/"
dirs = os.listdir(path)
print(dirs)
print(len(dirs))

for i in range(1,len(dirs),2):
    print(path+dirs[i])
