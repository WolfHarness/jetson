# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第217-218页 (PDF第227页, PDF第228页)
# 上下文: 在代码初始化部分将蜂鸣器控制引脚设置为高电平，以免误报。 ／ 2. 代码实现

import Jetson.GPIO as GPIO
import time

# 定义蜂鸣器引脚
PIN_BUZZER = 22
# 设置使用的引脚编码模式
GPIO.setmode(GPIO.BOARD)

# 初始化引脚为输出
# 低电平触发，初始为高电平，防止误操作
GPIO.setup(PIN_BUZZER, GPIO.OUT, initial=GPIO.HIGH)
