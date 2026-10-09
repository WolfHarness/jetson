# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第239-240页 (PDF第249页, PDF第250页)
# 上下文: ObjectDetector（Jetson-Inference 目标检测）两个工具类，最终实现AI 视觉控制两轮机器人。 ／ 里构建核心控制类TargetTra

#!/usr/bin/python3
# Jetson-inference和L298N 两轮小车视觉控制系统

import Jetson.GPIO as GPIO
import time
import cv2
import numpy as np
from collections import deque

class TargetTrackingCar:

    def __init__(self,
                 # 电机控制参数
                 forward_speed=50,
                 backward_speed=40,
                 turn_offset=25,
                 # 目标检测参数
                 target_class_id=1,
                 detect_threshold=0.5,
                 camera_path="v4l2:///dev/video0",
                 window_size=(640, 480),
                 # 跟踪策略参数
                 x_offset_threshold=50,    # X轴偏移阈值（像素）
                 y_offset_threshold=30,    # Y轴偏移阈值（像素）
                 lost_target_stop_delay=2  # 丢失目标后停止延迟（秒）
                 ):
        # 初始化子模块
        self.motor_ctrl = MotorController()
        self.detector = ObjectDetector(
            target_class_id=target_class_id,
            threshold=detect_threshold,
            camera_path=camera_path,
            window_width=window_size[0],
            window_height=window_size[1]
        )

        # 跟踪参数
        self.x_offset_threshold = x_offset_threshold
        self.y_offset_threshold = y_offset_threshold
        self.forward_speed = forward_speed
        self.backward_speed = backward_speed
        self.turn_offset = turn_offset
        self.lost_target_stop_delay = lost_target_stop_delay

        # 状态变量
        self.last_target_time = time.time()
        self.running = False
