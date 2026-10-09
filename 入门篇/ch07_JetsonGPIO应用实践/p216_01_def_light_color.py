# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第216页 (PDF第226页)
# 上下文: 为方便同时控制3 个LED 亮/ 灭，在此构建一个函数。

# 构建点亮指定颜色的函数
def light_color(red, green, blue):
    """
点亮指定颜色的RGB灯珠
:param red: 控制红色的GPIO信号（GPIO.LOW：灭。GPIO.HIGH：亮）
:param green: 控制绿色的GPIO信号（GPIO.LOW：灭。GPIO.HIGH：亮）
:param blue: 控制蓝色的GPIO信号（GPIO.LOW：灭。GPIO.HIGH：亮）
"""
    GPIO.output(R_PIN, red)  # 控制红色LED
    GPIO.output(G_PIN, green)  # 控制绿色LED
    GPIO.output(B_PIN, blue)  # 控制蓝色LED
