# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第210页 (PDF第220页)
# 上下文: 上述代码将GPIO 设置为BOARD 模式，也可以将其设置为BCM 模式，参考如下代码。 ／ 式，即物理引脚编号模式。

#将GPIO模式设置为BCM模式
GPIO.setmode(GPIO.BCM)
