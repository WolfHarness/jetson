# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第241-242页 (PDF第251页, PDF第252页)
# 上下文: 导致的频繁启停，提升跟踪稳定性。 ／ 对于未检测到目标的情况，系统会通过计时判断是否超过设定延迟，避免因短暂遮挡

    def _decision_making(self, detect_result):
        """根据检测结果决策小车运动方向"""
        current_time = time.time()

        # 检测到目标
        if detect_result['target_found']:
            self.last_target_time = current_time
            diff_x = detect_result['diff_x']
            diff_y = detect_result['diff_y']

            # 横向控制（左右转向）
            if abs(diff_x) > self.x_offset_threshold:
                if diff_x > 0:  # 目标在右侧，右转
                    self.motor_ctrl.car_right_turn(
                        base_speed=self.forward_speed,
                        offset=self.turn_offset
                    )
                    print(f"跟踪决策：目标偏右（{diff_x:.1f}）→ 右转")
                else:  # 目标在左侧，左转
                    self.motor_ctrl.car_left_turn(
                        base_speed=self.forward_speed,
                        offset=self.turn_offset
                    )
                    print(f"跟踪决策：目标偏左（{diff_x:.1f}）→ 左转")

            # 纵向控制（前进/后退）
            elif abs(diff_y) > self.y_offset_threshold:
                if diff_y > 0:  # 目标偏下，前进
                    self.motor_ctrl.car_forward(speed=self.forward_speed)
                    print(f"跟踪决策：目标偏下（{diff_y:.1f}）→ 前进")
                else:  # 目标偏上，后退
                    self.motor_ctrl.car_backward(speed=self.backward_speed)
                    print(f"跟踪决策：目标偏上（{diff_y:.1f}）→ 后退")

            # 目标居中，停止
            else:
                self.motor_ctrl.car_stop()
                print("跟踪决策：目标居中 → 停止")

        # 未检测到目标
        else:
            if current_time - self.last_target_time > self.lost_target_stop_delay:
                self.motor_ctrl.car_stop()
                print(f"跟踪决策：丢失目标超过{self.lost_target_stop_delay}秒 → 停止")
