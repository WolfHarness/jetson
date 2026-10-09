# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第231-232页 (PDF第241页, PDF第242页)
# 上下文: 最后，释放GPIO 资源。

    def cleanup(self):
        """释放所有硬件资源"""
        print("资源释放：开始清理...")
        try:
            # 1. 停止电机
            self.car_stop()

            # 2. 手动释放PWM资源
            if self.pwm_left:
                self.pwm_left.stop()
                if hasattr(self.pwm_left._ch_info, 'f_duty_cycle'):
                    try:
                        self.pwm_left._ch_info.f_duty_cycle.close()
                    except: pass
                del self.pwm_left
                self.pwm_left = None

            if self.pwm_right:
                self.pwm_right.stop()
                if hasattr(self.pwm_right._ch_info, 'f_duty_cycle'):
                    try:
                        self.pwm_right._ch_info.f_duty_cycle.close()
                    except: pass
                del self.pwm_right
                self.pwm_right = None

            gc.collect()
            print("资源释放：PWM清理完成")

        except Exception as e:
            print(f"PWM释放警告：{str(e)}")

        finally:
            # 3. 清理GPIO
            if self.gpio_initialized:
                try:
                    # 重置引脚为输入模式
                    for pin in [self.IN1, self.IN2, self.IN3, self.IN4, self.ENA, self.ENB]:
                        GPIO.setup(pin, GPIO.IN)

                    GPIO.cleanup()
                    self.gpio_initialized = False
                    print("资源释放：GPIO清理完成")
                except Exception as e:
                    print(f"GPIO释放警告：{str(e)}")
            print("资源释放：流程结束")
