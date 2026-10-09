# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第233页 (PDF第243页)
# 上下文: 位置偏差。 ／ 识别指定类别的目标并计算其与屏幕中心的

#!/usr/bin/python3
# Jetson-inference目标检测器
import jetson_inference
import jetson_utils
import time
import cv2
import numpy as np
