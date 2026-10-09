# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第218页 (PDF第228页)
# 上下文: 最后，调用该函数，并清理GPIO 设置。 ／ 构建一个函数，通过循环触发蜂鸣器发出警报。

buzzer()
# 清理GPIO
GPIO.cleanup()
