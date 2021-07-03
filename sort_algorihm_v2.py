'''''''''
@file: sort_algorihm_v1.py
@author: MRL Liu
@time: 2021/6/30 21:11
@env: Python,Numpy,copy
@desc:经典排序算法的实现(基于sortdrawer_v2)
@ref:无
@blog: https://blog.csdn.net/qq_41959920
'''''''''
from sortdrawer_v2 import Drawer,Frame
import copy

# 冒泡排序
def bubble_sort(init_frame):
    assert isinstance(init_frame, Frame), "Type Error"  # 进行安全检查
    frames = [init_frame]  # 添加初始帧
    ds = copy.deepcopy(init_frame)  # 复制第一帧
    length = len(ds.data)  # 获取该帧的数据
    for i in range(1, length):
        for j in range(0, length - i):
            if ds.data[j] > ds.data[j + 1]:
                ds.data[j], ds.data[j + 1] = ds.data[j + 1], ds.data[j]# 交换数据
                frames.append(Frame.get_new_frame(ds.data,[j,j+1]))  # 加入新的一帧
    return frames

# 选择排序
def selection_sort(init_frame):
    assert isinstance(init_frame, Frame), "Type Error"  # 进行安全检查
    frames = [init_frame]  # 添加初始帧
    ds = copy.deepcopy(init_frame)  # 复制第一帧
    length = len(ds.data)  # 获取该帧的数据
    for i in range(0, length-1):
        index = i
        for j in range(i+1, length):
            if ds.data[index] > ds.data[j]:
                index = j
        if index != i:
            ds.data[index], ds.data[i] = ds.data[i], ds.data[index]# 交换数据
            frames.append(Frame.get_new_frame(ds.data,[index,i]))  # 加入新的一帧
    return frames

# 插入排序
def insertion_sort(init_frame):
    assert isinstance(init_frame, Frame), "Type Error"  # 进行安全检查
    frames = [init_frame]  # 添加初始帧
    ds = copy.deepcopy(init_frame)  # 复制第一帧
    length = len(ds.data)  # 获取该帧的数据
    for i in range(0, length):
        preIndex = i-1
        current = ds.data[i]
        while preIndex>=0 and current<ds.data[preIndex]:
            ds.data[preIndex+1]=ds.data[preIndex]
            preIndex-=1
            frames.append(Frame.get_new_frame(ds.data, [preIndex+1,preIndex]))  # 加入新的一帧
        ds.data[preIndex+1] = current
        frames.append(Frame.get_new_frame(ds.data, [preIndex]))  # 加入新的一帧
    return frames

if __name__=='__main__':
    # 创建绘制器
    drawer = Drawer(100) # 参数控制排序速度（ms）
    # 创建一个32个数的初始帧
    initFrame = Frame.get_init_frame(30)
    # 排序生成一组帧
    frames = bubble_sort(initFrame)
    #frames = selection_sort(initFrame)
    #frames = insertion_sort(initFrame)
    # 显示帧
    drawer.show(frames)
    # 保存帧
    #drawer.save(frames,'./sortdrawer_v2.gif')