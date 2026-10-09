# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第119页 (PDF第129页)
# 上下文: 使用FFmpeg 等工具测试视频设备，确保它可以正常工作，可参考如下命令。 ／ 3. 测试视频设备

ffmpeg -f v4l2 -i /dev/video2 -f x11grab -r 30 -s 640x480 -i :0.0 -pix_fmt yuv420p -vcodec libx264 -preset ultrafast -t 00:00:10 output.mp4
