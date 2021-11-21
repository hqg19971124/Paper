# -*-coding:utf-8 -*-
'''
author:侯清刚
datetime:2021年11月20日
'''
import os


def geturlPath():
    # 指定路径
    path = './Dataset/test/center'
    # 返回指定路径的文件夹名称
    dirs = os.listdir(path)
    # 循环遍历该目录下的照片
    for dir in dirs:
        # 拼接字符串
        pa = path + dir
        # 判断是否为照片
        if not os.path.isdir(pa):
            # 使用生成器循环输出
            yield pa


if __name__ == '__main__':
    img_path_list=[]
    for item in geturlPath():
        img_path_list.append(item)
    print(len(img_path_list))