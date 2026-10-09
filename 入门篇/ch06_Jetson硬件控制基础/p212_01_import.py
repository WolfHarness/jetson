# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第212页 (PDF第222页)
# 上下文: 度等。使用 GPIO.PWM() 方法即可实现PWM 信号输出，完成上述控制。 ／ 号。例如，通过调节占空比，可以模拟出不同电压的平均值，用于控制电机转速、LE

import Jetson.GPIO as GPIO
import time
#将GPIO模式设置为BOARD模式
GPIO.setmode(GPIO.BOARD)
#将引脚33设置为PWM输出
PWM_PIN = 33
GPIO.setup(PWM_PIN, GPIO.OUT)
# 初始化 PWM，将频率设置为50Hz
pwm = GPIO.PWM(PWM_PIN, 50)

# 启动 PWM，初始占空比为 0%
pwm.start(0)
try:
    # 改变占空比，并实时打印当前占空比
    for duty_cycle in range(0, 101, 10):    # 从0到100每次增加10
        pwm.ChangeDutyCycle(duty_cycle)     # 设置占空比
        print(f"当前占空比: {duty_cycle}%")  # 输出占空比
        time.sleep(1)  # 等待1s
    # 假设占空比完成变化后停止
    pwm.stop()
except KeyboardInterrupt:
    # 处理 Ctrl+C 终止程序
    print("程序中断，停止 PWM 输出")
    pwm.stop()
finally:
    # 清理GPIO
    GPIO.cleanup()
