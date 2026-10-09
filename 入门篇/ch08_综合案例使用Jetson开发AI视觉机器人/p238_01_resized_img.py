# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第238页 (PDF第248页)

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
