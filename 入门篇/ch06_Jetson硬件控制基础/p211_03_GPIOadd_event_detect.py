# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第211页 (PDF第221页)
# 上下文: 化时触发。 ／ Jetson.GPIO 库提供了事件检测功能，我们可以设置一个回调函数，在引脚状态发生变

# 将引脚 7 设置为输入模式，并启用事件检测（当按钮被按下时触发）
GPIO.add_event_detect(7, GPIO.FALLING, callback=my_callback_function)
# 事件回调函数
def my_callback_function(channel):
    print("Button pressed!")
