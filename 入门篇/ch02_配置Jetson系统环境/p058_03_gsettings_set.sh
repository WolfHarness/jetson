# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第058页 (PDF第68页)
# 上下文: 执行以下命令来配置VNC 服务，使其能打开桌面共享。 ／ （3）配置VNC 服务

# 配置VNC server
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
