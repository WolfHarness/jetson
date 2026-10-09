# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第211页 (PDF第221页)
# 上下文: GPIO 引脚共有高、低两种状态，可以通过以下代码获取GPIO 引脚状态。 ／ 3. 读取引脚状态

state = GPIO.input(7)
if state == GPIO.HIGH:
    print("引脚是高电平")
elif state == GPIO.LOW:
    print("引脚是低电平")
