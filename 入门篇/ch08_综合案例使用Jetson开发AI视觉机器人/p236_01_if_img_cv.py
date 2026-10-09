# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第236页 (PDF第246页)

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
