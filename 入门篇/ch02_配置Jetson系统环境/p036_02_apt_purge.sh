# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第036页 (PDF第46页)
# 上下文: 若需将office、游戏等软件卸载，可以执行如下命令。 ／ 建议在完成上述系统更新任务后，卸载或清理不常用的软件。Jetson 设备储存空间有限，

# 卸载office工具（约占用300MB系统内存）和游戏
sudo apt purge -y \
    libreoffice* \
    gnome-mahjongg \
    gnome-sudoku\
    aisleriot \
    gnome-mines
