# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第220页 (PDF第230页)
# 上下文: 图7-6Jetson GPIO 实现倒车雷达 ／ PIN1

# 定义Trig和Echo引脚
TRIG = 16
ECHO = 18
# 设置Trig和Echo引脚的输入输出模式
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
