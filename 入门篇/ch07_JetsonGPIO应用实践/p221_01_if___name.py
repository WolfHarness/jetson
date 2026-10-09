# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第221页 (PDF第231页)
# 上下文: 距离，亮红灯，并使用蜂鸣器报警，这将使用到前文部分代码。 ／ 我们期望，当距离大于15cm 时视为安全距离，亮绿灯；当距离小于15cm 时视为危险

if __name__ == '__main__':
    try:
        while True:
            distance = get_distance()
            print("距离: {} cm".format(distance))
            if distance > 15: # 安全
                # 亮绿灯
                light_color(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
                time.sleep(1)
            else: # 危险
                # 亮红灯
                light_color(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
                buzzer() # 蜂鸣器报警
                time.sleep(1)

    except KeyboardInterrupt:
        print("程序被中断")
        GPIO.cleanup()  # 清理GPIO配置
