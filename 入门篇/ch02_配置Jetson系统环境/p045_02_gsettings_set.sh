# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第045页 (PDF第55页)
# 上下文: Terminator，可以执行如下命令。 ／ Ubuntu 系统可以使用快捷键<Ctrl+Alt+T> 开启默认终端，如果想要使用该快捷键打开

# 设置快捷键<Ctrl+Alt+T>开启Terminator

gsettings set org.gnome.desktop.default-applications.terminal exec /usr/bin/terminator
gsettings set org.gnome.desktop.default-applications.terminal exec-arg "-x"
