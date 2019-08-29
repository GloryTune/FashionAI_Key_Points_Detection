# a = [1,2,3,4]
# b = [2,3]
# for i in b:
#     if i in a:
#         print(i)
import pandas as pd
import shutil
import csv
import os
acsv = pd.read_csv('/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/test_b.csv',usecols=[0])
acsv.to_csv('/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/acsv.csv',index=False)
blouse_csv = pd.read_csv('/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/acsv.csv')
test1 = blouse_csv.iloc[8024:9970,:]#按种类分
print(test1)
test1.to_csv('/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/trousers.csv',index=False)

with open('/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/trousers.csv') as csvfile:
    reader = csv.reader(csvfile)
    #rows = [row for row in reader]
    blouse_list = []
    for i in reader:
        blouse_list.append(i)
del blouse_list[0]
print(blouse_list,len(blouse_list))

b_list = []
for o in blouse_list:
    q = o[0].split('/')
    b_list.append(q[2])
print(b_list)
blouse_path ='/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/train/Images/trousers'
blouse_file_list =os.listdir(blouse_path)
val_blouse ='/home/tianyou/PycharmProjects/FashionAI_Key_Points_Detection/data/val/Images/trousers'
for item in blouse_file_list:
    if item in b_list:
        shutil.copyfile(os.path.join(blouse_path,item),os.path.join(val_blouse,item))
        print('正在分类')
print('完毕')