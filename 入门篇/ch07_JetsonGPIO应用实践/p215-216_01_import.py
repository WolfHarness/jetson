# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第215-216页 (PDF第225页, PDF第226页)
# 上下文: 式，并绑定GPIO 引脚地址。 ／ 我们先进行初始化，将GPIO 设置为BOARD 模式，将RGB 灯珠引脚设置为输出模

import Jetson.GPIO as GPIO
import time

# 设置GPIO模式为BOARD
GPIO.setmode(GPIO.BOARD)
R_PIN = 29 # 红色引脚
G_PIN = 31 # 绿色引脚
B_PIN = 33 # 蓝色引脚
# 配置RGB灯珠的引脚
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)
