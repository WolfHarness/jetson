# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第229页 (PDF第239页)
# 上下文: 高低位信号，控制电机转动方向。 ／ 这里构建电机转向控制实现方法set_motor_direction，通过控制L298N 的IN1 ～IN4

    def set_motor_direction(self, motor, direction):
        """设置单个电机转向
        motor: 'left'/'right'
        direction: 'forward'/'backward'/'stop'
        """
        if not self.gpio_initialized:
            return

        try:
            if motor == 'left':
                # 左电机：IN1高+IN2低=前进；IN1低+IN2高=后退
                GPIO.output(self.IN1, GPIO.HIGH if direction == 'forward' else GPIO.LOW)
                GPIO.output(self.IN2, GPIO.HIGH if direction == 'backward' else GPIO.LOW)
            else:
                # 右电机：IN3高+IN4低=前进；IN3低+IN4高=后退
                GPIO.output(self.IN3, GPIO.HIGH if direction == 'forward' else GPIO.LOW)
                GPIO.output(self.IN4, GPIO.HIGH if direction == 'backward' else GPIO.LOW)
        except Exception as e:
            print(f"方向控制错误（{motor}）：{str(e)}")
