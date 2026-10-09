# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第234-235-236页 (PDF第244页, PDF第245页, PDF第246页)
# 上下文: 添加各种可视化元素并显示图像。 ／ 与屏幕中心的偏移量，将图像转换为 OpenCV 兼容的格式并调整大小，最后调用绘图函数

    def process_frame(self):
        """
        处理一帧图像，进行目标检测
        :return: 包含目标坐标和差值的字典
        """
        # 捕获图像
        img = self.camera.Capture()

        if img is None:
            return {
                'target_found': False,
                'target_x': None,
                'target_y': None,
                'screen_center_x': self.screen_center_x,
                'screen_center_y': self.screen_center_y,
                'diff_x': 0,
                'diff_y': 0,
                'fps': None
            }

        # 更新屏幕中心坐标（基于实际图像尺寸）
        self.screen_center_x = img.width / 2
        self.screen_center_y = img.height / 2

        # 目标检测
        detections = self.net.Detect(img)

        # 重置目标坐标
        self.target_x = None
        self.target_y = None
        target_found = False

        # 查找目标
        for detection in detections:
            if detection.ClassID == self.target_class_id:
                self.target_x = detection.Center[0]
                self.target_y = detection.Center[1]
                target_found = True
                break  # 只取第一个目标

        # 计算差值
        if target_found:
            self.diff_x = self.target_x - self.screen_center_x
            self.diff_y = self.target_y - self.screen_center_y

            # 仅在检测到目标时更新FPS计数
            self.frame_count += 1
            self._update_fps()
        else:
            self.diff_x = 0
            self.diff_y = 0

        # 将CUDA图像转换为OpenCV格式并处理
        img_cv = jetson_utils.cudaToNumpy(img)
        if img_cv is not None:
            # 转换颜色空间 (RGBA -> BGR)
            if img_cv.shape[2] == 4:
                img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGBA2BGR)
            elif img_cv.shape[2] == 3:
                img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

            # 确保图像适应窗口大小（保持比例）
            img_cv = self._resize_image(img_cv, self.window_width, self.window_height)

            # 绘制叠加层
            self._draw_overlay(img_cv, target_found)

            # 显示图像
            cv2.imshow(self.window_name, img_cv)

            # 检查按键，按'q'键退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_detection()

        # 返回检测结果
        return {
            'target_found': target_found,
            'target_x': self.target_x,
            'target_y': self.target_y,
            'screen_center_x': self.screen_center_x,
            'screen_center_y': self.screen_center_y,
            'diff_x': self.diff_x,
            'diff_y': self.diff_y,
            'fps': self.fps if target_found else None
        }
