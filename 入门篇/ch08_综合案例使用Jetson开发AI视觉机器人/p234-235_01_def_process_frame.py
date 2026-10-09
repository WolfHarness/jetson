# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第234-235页 (PDF第244页, PDF第245页)
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
