# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第210页 (PDF第220页)
# 上下文: GPIO 引脚可以配置为输入/ 输出模式，使用 GPIO.setup() 来设置，参考如下代码。 ／ 2. GPIO 引脚输入/ 输出模式

# 将引脚设置为输入模式
GPIO.setup(7, GPIO.IN, initial=GPIO.HIGH)
# 将引脚设置为输出模式
GPIO.setup(8, GPIO.OUT)
