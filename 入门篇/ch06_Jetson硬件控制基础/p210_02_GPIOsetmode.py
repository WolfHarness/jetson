# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第210页 (PDF第220页)
# 上下文: 式，即物理引脚编号模式。 ／ GPIO 模式共有两种：BCM 模式和BOARD 模式。对于初学者，推荐使用BOARD 模

# 设置 GPIO 模式，BCM 或 BOARD（BCM: 引脚编号。BOARD: 板上物理引脚编号）
GPIO.setmode(GPIO.BOARD)
