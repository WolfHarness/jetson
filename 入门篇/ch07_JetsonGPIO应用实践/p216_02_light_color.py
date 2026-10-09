# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第7章 JetsonGPIO应用实践 · 印刷第216页 (PDF第226页)
# 上下文: 通过000 →111 高低电平编码来控制单个LED 灯的亮灭。 ／ 为方便同时控制3 个LED 亮/ 灭，在此构建一个函数。

# RGB单独依次亮、全亮、全灭
# 依次点亮红色、绿色、蓝色

# 红色亮
light_color(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
time.sleep(1)

# 绿色亮
light_color(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
time.sleep(1)

# 蓝色亮
light_color(GPIO.LOW, GPIO.LOW, GPIO.HIGH)
time.sleep(1)

# 全亮
light_color(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)
time.sleep(1)

# 全灭
light_color(GPIO.LOW, GPIO.LOW, GPIO.LOW)
