'''''''''
@file: SortDrawer_v2.py
@author: MRL Liu
@time: 2021/6/30 20:05
@env: Python,Numpy,opencv
@desc: 排序算法动画模块
@ref:
@blog: https://blog.csdn.net/qq_41959920
'''''''''
import copy
import random
import numpy as np
import time
import cv2
from PIL.Image import Image
import PIL

# 计时器
class Timer:
    def __init__(self):
        self.InitTime()

    def InitTime(self):
        self.start=time.time()
        self.time=0.0
        self.StopTimer()
    # 开始计时
    def StartTimer(self):
        self.start_flag=True
        self.start = time.time()

    # 结束计时
    def StopTimer(self):
        self.start_flag=False

    # 获取时间
    def GetTime(self):
        if self.start_flag:
            self.time = time.time()-self.start
        return self.time
# 帧
class Frame:
    bar_width = 5

    def __init__(self, img, data):
        self.img = img  # 图像矩阵
        self.data = data  # 数据列表
    @classmethod
    def get_init_frame(cls,data_count):
        # 生成数据
        data = list(range(1, data_count + 1))  # 生成数据
        random.shuffle(data)  # 随机打乱数据
        # 生成图像
        img_size = cls.bar_width * data_count # 图像尺寸
        img = np.full(shape=(img_size, img_size, 3), fill_value=255, dtype=np.uint8)  # 创建全黑矩阵
        # 更改图片像素矩阵的颜色
        for i in range(0, data_count):
            val = data[i]
            img[-val * cls.bar_width:, i * cls.bar_width:(i + 1) * cls.bar_width] = cls.get_color(val,data_count)
        return Frame(img,data)

    @classmethod
    def get_new_frame(cls,data,mark1):
        data_count = len(data)
        # 生成图像
        img_size = cls.bar_width * data_count  # 图像尺寸
        img = np.full(shape=(img_size, img_size, 3), fill_value=255, dtype=np.uint8)  # 创建全黑矩阵
        # 更改图片像素矩阵的颜色
        for i in range(0, data_count):
            val = data[i]
            img[-val * cls.bar_width:, i * cls.bar_width:(i + 1) * cls.bar_width] = cls.get_color(val, data_count)
        cls.SetColor(img, mark1, (0, 0, 255),data,cls.bar_width)
        return Frame(img, data)

    @staticmethod
    def get_color(val, TOTAL):
        return (120 + val * 255 // (2 * TOTAL), 255 - val * 255 // (2 * TOTAL), 0)

    @staticmethod
    def SetColor(img, marks, color,data,bar_width):
        for idx in marks:
            min_col = idx*bar_width
            max_col = min_col+bar_width
            min_row = -1-data[idx]*bar_width
            img[min_row:, min_col:max_col] = color
# 绘制器
class Drawer:
    KEY_SPACE_INDEX=32 # 空格键的ASCII值
    KEY_ESC_INDEX = 27 # ESC键的ASCII值
    def __init__(self,time_interval=100):
        self.timer = Timer() # 计时器
        self.time_interval = time_interval # 帧之间的时间间隔（毫秒）

    # 显示图像
    def show(self,frames):
        self.timer.StartTimer()
        for frame in frames:
            img = frame.img
            cv2.putText(img=img,
                        text="Time:%02.2fs" % self.timer.GetTime(),
                        org=(20, 10),  # 左上角坐标
                        fontFace=cv2.FONT_HERSHEY_PLAIN,  # 字体
                        fontScale=1,  # 字体大小
                        color=(0, 127, 255))
            cv2.imshow(winname='OpenCV', mat=img)  # 显示图片窗口
            input_keyIndex = cv2.waitKey(self.time_interval)  # 单位毫秒，等待键盘输入，0表示一直等待
            if input_keyIndex == self.KEY_SPACE_INDEX or input_keyIndex == self.KEY_ESC_INDEX:
                print('您退出了测试')
                break
        self.timer.StopTimer()

    # 保存图像
    def save(self,frames,file='./result.gif'):
        _imgs=[]
        for frame in frames:
            _img = PIL.Image.fromarray(cv2.cvtColor(frame.img, cv2.COLOR_BGR2RGB))
            _imgs.append(_img)
        _imgs[0].save(file, save_all=True, append_images=_imgs, loop=100, duration=1)
        print('保存成功：'+file)



