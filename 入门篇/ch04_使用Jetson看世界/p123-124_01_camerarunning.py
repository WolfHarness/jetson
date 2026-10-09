# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第123-124页 (PDF第133页, PDF第134页)
# 上下文: 这时的画面只有一帧，所以是静态画面，可以参考如下代码使画面实时展现。 ／ 现在获取摄像头画面，并使用widget 将其展现在JupyterLab 中。

camera.running = True
def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)

# 开启观察者模式
camera.observe(update_image, names='value')
