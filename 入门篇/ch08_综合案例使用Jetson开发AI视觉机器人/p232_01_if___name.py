# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第232页 (PDF第242页)
# 上下文: 可以参考如下程序，使用Jetson 驱动L298N 两路电机控制。

# 测试程序
if __name__ == "__main__":
    motor_ctrl = None
    try:
        motor_ctrl = MotorController()
        print("测试启动：开始电机测试（13s）...")

        motor_ctrl.car_forward(50)
        time.sleep(3)

        motor_ctrl.car_backward(50)
        time.sleep(3)

        motor_ctrl.car_left(50)
        time.sleep(2)

        motor_ctrl.car_right(50)
        time.sleep(2)

        motor_ctrl.car_stop()
        time.sleep(3)

        print("测试完成：所有功能正常")

    except KeyboardInterrupt:
        print("测试中断：用户手动停止")
    except Exception as e:
        print(f"测试错误：{str(e)}")
    finally:
        if motor_ctrl:
            motor_ctrl.cleanup()
