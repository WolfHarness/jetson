# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第220-221页 (PDF第230页, PDF第231页)
# 上下文: 接下来，根据前文所述的测距公式来构建一个测距函数。 ／ 图7-6Jetson GPIO 实现倒车雷达

def get_distance():
    # 发送一个短的高电平脉冲来触发传感器
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)  # 等待稳定
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # 发送脉冲时间为10μs
    GPIO.output(TRIG, GPIO.LOW)

    # 计算Echo信号的返回时间
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    # 计算脉冲持续时间
    pulse_duration = pulse_end - pulse_start

    # 声速：34300 cm/s
    v = 34300 / 2
    distance = pulse_duration * v  # 计算距离 (cm)
    # 返回距离
    return round(distance, 2)
