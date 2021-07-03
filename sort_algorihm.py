'''''''''
@file: sort_algorihm.py
@author: MRL Liu
@time: 2021/7/1 20:37
@env: Python,Numpy
@desc: 经典排序算法的实现(附加详细的原理讲解)
@ref:
@blog: https://blog.csdn.net/qq_41959920
'''''''''
import random
import numpy as np

# 冒泡排序
def bubble_sort(data):
    length = len(data) # 获取待排序数组长度，用于遍历
    for i in range(1, length):
        for j in range(0, length - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# 选择排序
def Selection_Sort(data):
    length = len(data) # 获取待排序数组长度，用于遍历
    for i in range(0,length-1):
        minIndex = i
        for j in range(i+1, length):
            if data[j]>data[minIndex]:
                minIndex = j
        if minIndex != i:
            data[minIndex],data[i] = data[i],data[minIndex] # 交换两个数
    return data

# 插入排序（扑克）
def Insertion_Sort(data):
    length = len(data)  # 获取待排序数组长度，用于遍历
    for i in range(0,length):
        preIndex = i - 1 # 最后一个已排序数字的序号
        current = data[i] # 保存当前选中的数字
        while preIndex >= 0 and data[preIndex] > current:# 当前数字小于最后一个已排序数字
            data[preIndex + 1] = data[preIndex] # 已排序数字后移
            preIndex -= 1 # 最后已排序序号前移
        data[preIndex + 1] = current
    return data

if __name__=="__main__":
    #random.seed(0)
    data = [x for x in range(30)] # 构建待排序的数组
    #random.shuffle(data) # 将数据打乱
    print(data) # 打印该数组

    #data = bubble_sort(data) # 冒泡排序
    #data = Selection_Sort(data) # 选择排序
    data = Insertion_Sort(data) # 插入排序
    print(data) # 打印该数组