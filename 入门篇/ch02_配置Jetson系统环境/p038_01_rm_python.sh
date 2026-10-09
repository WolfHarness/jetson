# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第038页 (PDF第48页)
# 上下文: 下面，执行如下命令，将“python”命令由指向Python 2.7 改为指向Python 3.8。 ／ 图2-28 修正软链接前的Python 2 和Pyth

# 修正python3软链接
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
