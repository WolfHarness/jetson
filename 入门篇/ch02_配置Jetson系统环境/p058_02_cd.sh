# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第058页 (PDF第68页)
# 上下文: 我们可以在用户主目录下执行以下命令创建自启动服务。 ／ 单击图2-57 所示的“Screen Sharing”无法正常使用是因为未能打开Vino 的使能开关，

# 创建符号链接
cd ~/
sudo ln -s ../vino-server.service   /usr/lib/systemd/user/graphical-session.target.wants
