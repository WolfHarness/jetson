# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第229页 (PDF第239页)
# 上下文: 为。 ／ GPIO 清理流程冲突（导致“坏文件描述符”错误），因此通过覆写析构函数禁用这一自动行

    def _override_pwm_destructor(self, pwm_obj):
        """替换PWM析构函数为空白实现"""
        def dummy_del(self):
            pass
        pwm_obj.__del__ = dummy_del.__get__(pwm_obj, type(pwm_obj))
