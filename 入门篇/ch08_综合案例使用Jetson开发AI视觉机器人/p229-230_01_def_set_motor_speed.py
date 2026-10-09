# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第229-230页 (PDF第239页, PDF第240页)
# 上下文: 脚PWM 信号，控制电机转速。 ／ 这里构建电机转速控制实现方法set_motor_speed，通过控制L298N 的ENA、ENB 引

    def set_motor_speed(self, motor, speed):
        """设置电机速度（占空比0~100）"""
        if not self.gpio_initialized:
            return

        try:
            speed = max(0, min(100, speed))  # 限制速度范围
            if motor == 'left' and self.pwm_left:
                self.pwm_left.ChangeDutyCycle(speed)
            elif motor == 'right' and self.pwm_right:
                self.pwm_right.ChangeDutyCycle(speed)
        except Exception as e:
            print(f"速度控制错误（{motor}）：{str(e)}")

    def control_motor(self, motor, direction, speed):
        """合并控制电机转向和速度"""
        self.set_motor_direction(motor, direction)
        self.set_motor_speed(motor, speed)
