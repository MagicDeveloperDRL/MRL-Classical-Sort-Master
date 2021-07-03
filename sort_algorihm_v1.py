'''''''''
@file: sort_algorihm_v1.py
@author: MRL Liu
@time: 2021/6/30 21:11
@env: Python,Numpy
@desc: 经典排序算法的实现(基于sortdrawer_v1)
@ref: 无
@blog: https://blog.csdn.net/qq_41959920
'''''''''
from sortdrawer_v1 import SortDrawer
import copy
# 冒泡排序
def bubble_sort(init_frame):
    frames = [init_frame] # 添加初始帧
    ds = copy.deepcopy(init_frame) # 复制第一帧
    length = len(ds) # 获取该帧的数据
    for i in range(1,length):
        for j in range(0,length-i):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j] # 交换数据
                frames.append(copy.deepcopy(ds)) # 加入新的一帧
    frames.append(ds) # 添加初始帧
    return frames
# 选择排序
def selection_sort(init_frame):
    frames = [init_frame] # 添加初始帧
    ds = copy.deepcopy(init_frame) # 复制第一帧
    length = len(ds) # 获取该帧的数据
    for i in range(0,length-1):
        index = i
        for j in range(i+1,length):
            if ds[index].value > ds[j].value:
                index = j
        if index!=i:
            ds[index], ds[i] = ds[i], ds[index]  # 交换数据
            frames.append(copy.deepcopy(ds))  # 加入新的一帧
    frames.append(ds) # 添加初始帧
    return frames

# 插入排序
def insertion_sort(init_frame):
    frames = [init_frame] # 添加初始帧
    ds = copy.deepcopy(init_frame) # 复制第一帧
    length = len(ds) # 获取该帧的数据
    for i in range(0,length):
        preIndex = i-1 # 最后一个已排序数字的序号
        current = ds[i].value # 保存当前选中的数字
        while preIndex>=0 and current<ds[preIndex].value: # 当前数字小于最后一个数字时
            ds[preIndex+1].value = ds[preIndex].value # 后移
            preIndex-=1 # 序号减一
            frames.append(copy.deepcopy(ds))  # 加入新的一帧
        ds[preIndex + 1].value = current
        frames.append(copy.deepcopy(ds))  # 加入新的一帧
    frames.append(ds) # 添加初始帧
    return frames

if __name__=="__main__":
    # 创建绘制器
    drawer = SortDrawer('排序算法过程可视化')
    # 创建数据
    random_value = drawer.get_random_data(30)
    # 创建初始帧
    init_frame = drawer.get_init_frame(random_value)
    # 进行排序,生成多帧
    frames = insertion_sort(init_frame) # 排序
    # 设置动画
    drawer.set_animate(frames,10)
    # 保存动画
    #drawer.save_as_gif()
    # 显示动画
    drawer.show()