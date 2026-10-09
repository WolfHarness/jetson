# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第238-239页 (PDF第248页, PDF第249页)
# 上下文: 性，又提供了灵活的操作接口，使得该类能够适应多种应用场景。 ／ 提供了单帧检测的功能，满足不同场景下的使用需求。整体设计既考虑了实时检测的连续

    def start_detection(self):
        """启动连续目标检测循环"""
        self.running = True
        print(f"开 始 目 标 检 测... 窗 口 大 小: {self.window_width}x{self.window_height}")
        print("按 'q' 键退出检测")
        print("仅在检测到目标时显示日志信息...")

        try:
            while self.running:
                # 处理一帧并获取结果
                result = self.process_frame()

                # 仅在检测到目标时打印日志
                if result['target_found']:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{timestamp} - 目标坐标: ({int(result['target_x'])}, {int(result['target_y'])}) "
                          f"| 差值: (x: {result['diff_x']:.1f}, y: {result['diff_y']:.1f}) "
                          f"| FPS: {result['fps']:.1f}")

                # 短暂延迟，降低CPU占用率
                time.sleep(0.001)

        except KeyboardInterrupt:
            print("检测已停止")
        finally:
            self.stop_detection()

    def stop_detection(self):
        """停止目标检测"""
        self.running = False
        print("目标检测已停止")

        # 释放资源
        cv2.destroyWindow(self.window_name)
        cv2.destroyAllWindows()
        try:
            self.camera.Close()
        except:
            pass

    def get_single_frame_result(self):
        """获取单帧检测结果，用于非循环模式"""
        return self.process_frame()
