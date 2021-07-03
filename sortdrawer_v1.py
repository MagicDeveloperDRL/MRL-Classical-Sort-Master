'''''''''
@file: SortDrawer_v1.py
@author: MRL Liu
@time: 2021/7/1 20:32
@env: Python,Numpy,matplotlib,random,copy
@desc: 排序算法动画模块
@ref:https://blog.csdn.net/sinat_36772813/article/details/77449122
    https://blog.csdn.net/shelgi/article/details/100554760
@blog: https://blog.csdn.net/qq_41959920
'''''''''
from matplotlib import pyplot as plt
from matplotlib import animation
import random


# 单个数字
class Single_Nubmer:
    def __init__(self, value, rgb):
        self.value = value # 数字的数值
        self.color = rgb # 数字的颜色



# 排序绘制器
class SortDrawer:
    def __init__(self,win_name):
        self.fig = plt.figure(1, figsize=(6, 3))  # 创建窗口
        self.fig.canvas.set_window_title(win_name)  # 设置窗口标题
        self.ax = self.fig.add_subplot(111) # 添加画布
        self.ax.set_xticks([])  # 设置x刻度为空
        self.ax.set_yticks([])  # 设置y刻度为空
    # 创建原始数据
    @classmethod
    def get_random_data(self,data_count):
        data = list(range(1, data_count + 1))  # 生成数据
        random.shuffle(data)  # 随机打乱数据
        return data
    # 创建原始颜色
    def _get_random_color(self,data_count):
        colors = [(0.5,random.uniform(0,1),random.uniform(0.11,0.99)) for i in range(1,data_count + 1)]  # 生成颜色数据
        return colors
    # 构建初始帧数据
    def get_init_frame(self, data):
        data_count = len(data)
        return [Single_Nubmer(val, rgb) for val, rgb in zip(data, self._get_random_color(data_count))]

    # 设置动画过程
    def set_animate(self,frames,frame_interval=100):
        self.frames = frames
        self.x_data = list(range(len(self.frames[0]))) # x数据不变
        self.anim = animation.FuncAnimation(self.fig, self.anim_update, frames=len(self.frames), interval=frame_interval)


    # 显示动画过程
    def show(self):
        plt.show()

    # 动画更新函数(只能接受一个参数)
    def anim_update(self,fi):
        self.ax.cla()  # 清楚整个画布
        y_data = [d.value for d in self.frames[fi]]
        color = [d.color for d in self.frames[fi]]
        # 绘制柱状图
        bar = self.ax.bar(self.x_data, y_data, width=1, color=color, alpha=0.6)
        # 设置数字标签
        for a, b in zip(self.x_data, y_data):
            plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=6)
        return bar

    def save_as_gif(self,file='SortDrawer.gif'):
        self.anim.save(file, writer='pillow')
        print(file + ' 保存成功.')

    def save_as_html(self,file='SortDrawer.html'):
        self.anim.save('%s' % (file), writer=animation.HTMLWriter(fps=25))
        print(file + ' 保存成功.')






