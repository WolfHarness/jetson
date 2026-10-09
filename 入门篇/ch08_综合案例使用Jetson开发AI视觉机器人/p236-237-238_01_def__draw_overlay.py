# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第236-237-238页 (PDF第246页, PDF第247页, PDF第248页)
# 上下文: 比例适应显示窗口，保持良好的视觉效果。 ／ 键信息。这些视觉元素帮助用户直观了解检测情况，而_resize_image 方法则确保图像能按

    def _draw_overlay(self, img_cv, target_found):
        """在图像上绘制十字线"""
        height, width = img_cv.shape[:2]

        # 绘制屏幕中心十字线
        cv2.line(img_cv, (0, int(self.screen_center_y)),
                (width, int(self.screen_center_y)), (0, 255, 0), 2)   # 绿色水平线
        cv2.line(img_cv, (int(self.screen_center_x), 0),
                (int(self.screen_center_x), height), (0, 255, 0), 2)  # 绿色垂直线

        # 如果检测到目标，绘制目标标记和信息
        if target_found:
            cross_size = 10
            # 目标中心红色十字
            cv2.line(img_cv,
                    (int(self.target_x) - cross_size, int(self.target_y)),
                    (int(self.target_x) + cross_size, int(self.target_y)),
                    (0, 0, 255), 2)  # 红色水平线
            cv2.line(img_cv,
                    (int(self.target_x), int(self.target_y) - cross_size),
                    (int(self.target_x), int(self.target_y) + cross_size),
                    (0, 0, 255), 2)  # 红色垂直线

            # 显示坐标文本
            coords_text = f"Target: ({int(self.target_x)}, {int(self.target_y)})"
            cv2.putText(img_cv, coords_text,
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)  # 黄色文本

            # 显示差值文本
            diff_text = f"Offset: (x: {self.diff_x:.1f}, y: {self.diff_y:.1f})"
            cv2.putText(img_cv, diff_text,
                       (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)  # 绿色文本

            # 显示FPS信息
            fps_text = f"FPS: {self.fps:.1f}"
            cv2.putText(img_cv, fps_text,
                       (img_cv.shape[1] - 120, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)  # 蓝色文本

    def _update_fps(self):
        """更新FPS计算，仅在检测到目标时进行"""
        current_time = time.time()
        elapsed = current_time - self.last_fps_time

        # 每秒钟更新一次FPS
        if elapsed >= 1.0:
            self.fps = self.frame_count / elapsed
            self.frame_count = 0
            self.last_fps_time = current_time

    def _resize_image(self, img, target_width, target_height):
        """保持比例调整图像大小以适应目标窗口"""
        h, w = img.shape[:2]

        # 计算缩放比例
        scale = min(target_width / w, target_height / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        # 调整大小
        resized_img = cv2.resize(img, (new_w, new_h))

        # 如果需要，添加边框以达到精确的目标尺寸
        if new_w < target_width or new_h < target_height:
            # 计算边框
            top = (target_height - new_h) // 2
            bottom = target_height - new_h - top
            left = (target_width - new_w) // 2
            right = target_width - new_w - left

            # 添加灰色边框
            resized_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right,
                cv2.BORDER_CONSTANT, value=[128, 128, 128])

        return resized_img
