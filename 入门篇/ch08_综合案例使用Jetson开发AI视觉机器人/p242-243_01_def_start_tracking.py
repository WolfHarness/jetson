# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第242-243页 (PDF第252页, PDF第253页)
# 上下文: 免硬件故障和资源占用问题。 ／ 异常情况下通过 stop_tracking 方法安全停止，释放电机 GPIO 资源和摄像头设备，避

def start_tracking(self):
    """启动目标跟踪主循环"""
    self.running = True
    self.detector.start_detection()
        print("\n跟踪小车：启动目标跟踪（按'q'键停止）")

    try:
        while self.running and self.detector.running:
            # 获取检测结果
            detect_result = self.detector.process_frame()

            # 决策与控制
            self._decision_making(detect_result)

            # 短暂延迟，降低CPU占用
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n跟踪小车：用户手动停止")
    except Exception as e:
        print(f"\n跟踪小车：错误：{str(e)}")
    finally:
        self.stop_tracking()

def stop_tracking(self):
    """停止跟踪并释放所有资源"""
    self.running = False
    print("跟踪小车：停止跟踪，释放资源...")

    # 停止电机
    self.motor_ctrl.car_stop()
    self.motor_ctrl.cleanup()

    # 停止检测
    self.detector.stop_detection()

    print("跟踪小车：所有资源已释放")
# 测试入口
if __name__ == "__main__":
    # 初始化跟踪小车（根据实际情况调整参数）
    tracking_car = TargetTrackingCar(
        forward_speed=55,
        turn_offset=30,
        camera_path="v4l2:///dev/video0",  # USB摄像头，CSI摄像头用"csi://0"
        detect_threshold=0.6,
        x_offset_threshold=60,
        lost_target_stop_delay=1.5
    )

    # 启动跟踪
    tracking_car.start_tracking()
