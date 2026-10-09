# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第079页 (PDF第89页)
# 上下文: METADATA 元数据信息文件。 ／ 读者可以参考如下代码构建OpenCV-Python METADATA 和OpenCV-Contrib-Python。

# 构建OpenCV-Python METADATA
mkdir -p ~/.local/lib/python3.8/site-packages/opencv_python-4.9.0.dist-info
touch ~/.local/lib/python3.8/site-packages/opencv_python-4.9.0.dist-info/METADATA

# 构建OpenCV-Contrib-Python METADATA
mkdir -p ~/.local/lib/python3.8/site-packages/opencv_contrib_python-4.9.0.dist-info
touch ~/.local/lib/python3.8/site-packages/opencv_contrib_python-4.9.0.dist-info/METADATA
