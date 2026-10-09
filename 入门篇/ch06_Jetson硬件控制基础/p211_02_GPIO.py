# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第211页 (PDF第221页)
# 上下文: 操作中出现冲突。 ／ 在程序结束时，需要调用 GPIO.cleanup() 来清理设置，释放 GPIO 引脚，防止在后续

# 清理所有设置
GPIO.cleanup()

# 清理特定引脚
GPIO.cleanup(15)  # 只清理引脚 15
