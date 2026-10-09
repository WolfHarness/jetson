# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第218页 (PDF第228页)
# 上下文: 构建一个函数，通过循环触发蜂鸣器发出警报。 ／ 图7-4Jetson GPIO 控制RGB 灯珠+ 蜂鸣器

def buzzer(count=3):
    i = 0
    while(i < count):
        # 播放0.5s声音
        GPIO.output(PIN_BUZZER, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(PIN_BUZZER, GPIO.HIGH)
        time.sleep(0.1)
        i += 1
