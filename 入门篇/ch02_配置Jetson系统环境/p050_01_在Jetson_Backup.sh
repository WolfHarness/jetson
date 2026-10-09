# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第050页 (PDF第60页)
# 上下文: 在Jetson_Backup.sh 的基础上稍作修改，构建Jetson 镜像恢复脚本，可参考如下内容。 ／ 1. 命令方式恢复Jetson 系统

#!/bin/bash

#####################################
# Jetson设备镜像恢复脚本
#
# 入参1：Jetson镜像文件，如Jetson_Backup_20240401.img
# 入参2：Jetson设备地址，如/dev/sdb
#####################################

# 镜像备份
# if=$1为备份文件名
# of=$2为设备号，可以使用lsblk查到的磁盘设备号
# bs=4M表示块大小为4MB，这可以提高烧录速度
# status=progress 可以显示烧录进度
# oflag=sync 确保所有数据都被写入设备
sudo dd if=$1 of=$2 bs=4M status=progress oflag=sync
