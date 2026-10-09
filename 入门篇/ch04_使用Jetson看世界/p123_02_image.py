# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第123页 (PDF第133页)
# 上下文: 现在获取摄像头画面，并使用widget 将其展现在JupyterLab 中。 ／ 设定摄像头画面为640×480 像素。

# 获取摄像头画面
image = camera.read()

# 展示画面
import ipywidgets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg

image_widget = ipywidgets.Image(format='jpeg')
image_widget.value = bgr8_to_jpeg(image)
display(image_widget)
