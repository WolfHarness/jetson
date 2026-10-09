# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第216页 (PDF第226页)
# 上下文: 最后一定要清理GPIO 设置，避免GPIO 引脚冲突。 ／ 通过000 →111 高低电平编码来控制单个LED 灯的亮灭。

# 清理GPIO设置
GPIO.cleanup()
