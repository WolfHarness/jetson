# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第227-228页 (PDF第237页, PDF第238页)
# 上下文: 封装与扩展。 ／ 在代码实现层面，我们来构建一个L298N 电机控制器MotorController，便于后续功能

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# L298N双电机控制器
# 控制小车运动及PWM速度调节
import Jetson.GPIO as GPIO
import time
import sys
import gc

class MotorController:
    """L298N电机控制器核心类"""

    def __init__(self):
        # 物理引脚定义（需与硬件接线对应）
        self.IN1 = 16  # 左电机方向1
        self.IN2 = 18  # 左电机方向2
        self.IN3 = 22  # 右电机方向1
        self.IN4 = 24  # 右电机方向2
        self.ENA = 32  # 左电机PWM使能
        self.ENB = 33  # 右电机PWM使能

        # 初始化参数
        self.PWM_FREQ = 1000  # PWM频率(1kHz)
        self.pwm_left = None   # 左电机PWM对象
        self.pwm_right = None  # 右电机PWM对象
        self.gpio_initialized = False  # 初始化状态标记

        self.setup_gpio()

    def setup_gpio(self):
        """初始化GPIO和PWM配置"""
        try:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)  # 使用物理引脚编号

            # 配置方向控制引脚（输出模式，初始低电平）
            GPIO.setup([self.IN1, self.IN2, self.IN3, self.IN4],
                      GPIO.OUT, initial=GPIO.LOW)

            # 配置PWM引脚并创建对象
            GPIO.setup([self.ENA, self.ENB], GPIO.OUT)
            self.pwm_left = GPIO.PWM(self.ENA, self.PWM_FREQ)
            self.pwm_right = GPIO.PWM(self.ENB, self.PWM_FREQ)

            # 覆盖PWM析构函数，避免自动释放错误
            self._override_pwm_destructor(self.pwm_left)
            self._override_pwm_destructor(self.pwm_right)

            # 启动PWM（初始占空比0）
            self.pwm_left.start(0)
            self.pwm_right.start(0)

            self.gpio_initialized = True
            print("初始化完成：GPIO和PWM就绪")
