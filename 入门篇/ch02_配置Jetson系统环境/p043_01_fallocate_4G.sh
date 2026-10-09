# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第043页 (PDF第53页)
# 上下文: 命令参考如下。 ／ 这里以Jetson Orin Nano 4GB 设备为例，需要为其设置大小为4GB 的交换空间，具体

# 为设备分配4GB交换空间
sudo fallocate -l 4G /swapfile

# 为swapfile分配权限
sudo chmod 600 /swapfile

# 格式化并启用swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 设置开机自动启用交换空间
sudo bash -c 'echo "/swapfile swap swap defaults 0 0" >> /etc/fstab'
