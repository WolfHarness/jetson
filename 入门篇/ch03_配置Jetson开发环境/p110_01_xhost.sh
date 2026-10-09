# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第110页 (PDF第120页)
# 上下文: 一个图形化测试，具体脚本内容如下。 ／ 下面，编写支持Docker 容器图形化界面操作的运行命令，并使用ROS 海龟仿真器做

#!/bin/bash
# Docker 运行脚本

#获得图形支持
xhost +

docker run \
    --name l4t-base-foxy \
    -it \
    --runtime nvidia \
    -e DISPLAY=$DISPLAY \
    --privileged \
    -v /lib/modules:/lib/modules \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --cap-add SYS_PTRACE \
    l4t-base-foxy:latest /bin/bash
