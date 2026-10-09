# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第230-231页 (PDF第240页, PDF第241页)
# 上下文: 停止等。 ／ 有了前面的基本实现，就可以构建小车完整的运动控制：前进、后退、左转、右转、

    def car_forward(self, speed=50):
        """小车前进（默认50%速度）"""
        self.control_motor('left', 'forward', speed)
        self.control_motor('right', 'forward', speed)
        print(f"前进（速度：{speed}%）")

    def car_backward(self, speed=50):
        """小车后退"""
        self.control_motor('left', 'backward', speed)
        self.control_motor('right', 'backward', speed)
        print(f"后退（速度：{speed}%）")

    def car_left(self, speed=50):
        """差速左转（左电机半速）"""
        self.control_motor('left', 'forward', speed//2)
        self.control_motor('right', 'forward', speed)
        print(f"左转（基础速度：{speed}%）")

    def car_right(self, speed=50):
        """差速右转（右电机半速）"""
        self.control_motor('left', 'forward', speed)
        self.control_motor('right', 'forward', speed//2)
        print(f"右转（基础速度：{speed}%）")

    def car_stop(self):
        """紧急停止"""
        if not self.gpio_initialized:
            return
        try:
            GPIO.output([self.IN1, self.IN2, self.IN3, self.IN4], GPIO.LOW)
            if self.pwm_left:
                self.pwm_left.ChangeDutyCycle(0)
            if self.pwm_right:
                self.pwm_right.ChangeDutyCycle(0)
            print("停止")
        except Exception as e:
            print(f"停止错误：{str(e)}")
