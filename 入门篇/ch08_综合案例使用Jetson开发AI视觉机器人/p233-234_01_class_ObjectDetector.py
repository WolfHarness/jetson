# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第233-234页 (PDF第243页, PDF第244页)
# 上下文: 图8-6Jetson-Inference 目标检测 ／ 位置偏差。

class ObjectDetector:

    def __init__(self, target_class_id=1, threshold=0.5, camera_path="v4l2:///dev/video0", 
                 window_width=640, window_height=480):
        """
        初始化目标检测器
        :param target_class_id: 要检测的目标类别ID，默认为1（人）
        :param threshold: 检测置信度阈值
        :param camera_path: 摄像头路径
        :param window_width: 显示窗口宽度
        :param window_height: 显示窗口高度
        """
        # 初始化参数
        self.target_class_id = target_class_id
        self.threshold = threshold
        self.camera_path = camera_path
        self.window_width = window_width
        self.window_height = window_height
        # 初始化检测网络
        self.net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=threshold)

        # 初始化摄像头
        try:
            self.camera = jetson_utils.videoSource(camera_path)
            print(f"摄像头初始化成功: {camera_path}")
        except Exception as e:
            print(f"摄像头初始化失败: {e}")
            raise

        # 屏幕中心坐标
        self.screen_center_x = 0
        self.screen_center_y = 0

        # 目标坐标
        self.target_x = None
        self.target_y = None

        # 坐标差值
        self.diff_x = 0
        self.diff_y = 0

        # FPS计算相关
        self.fps = 0.0
        self.frame_count = 0
        self.last_fps_time = time.time()

        # 运行状态
        self.running = False
        self.window_name = "Object Detection (640x480)"

        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, window_width, window_height)
