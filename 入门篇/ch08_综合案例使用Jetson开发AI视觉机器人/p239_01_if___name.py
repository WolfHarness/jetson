# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第239页 (PDF第249页)
# 上下文: 最后，参考如下代码，启动目标检测器。

# 示例用法
if __name__ == "__main__":
    # 创建检测器实例，使用640×480窗口
    detector = ObjectDetector(
        target_class_id=1,
        threshold=0.5,
        window_width=640,
        window_height=480
    )

    # 启动连续检测
    detector.start_detection()
