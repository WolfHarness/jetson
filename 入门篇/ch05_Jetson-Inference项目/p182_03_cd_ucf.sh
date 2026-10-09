# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第182页 (PDF第192页)
# 上下文: 任选一个视频文件，使用FFmpeg 对其格式进行转换，参考以下命令。 ／ Jetson-Inference 支持的数据格式。

cd ucf_sports_actions/ucf action/Diving-Side/001
# 视频格式转换
ffmpeg -i 2538-5_70133.avi -c:v libx264 -crf 23 -preset fast 2538-5_70133.mp4

# 移动视频文件
mv 2538-5_70133.mp4 ~/jetson-inference/data/videos
