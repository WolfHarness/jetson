# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第093页 (PDF第103页)

# 安装jupyter小部件扩展插件
sudo python3 -m pip install jupyterlab_widgets

# 安装必要插件
python3 -m pip install qtconsole
python3 -m pip install ipywidgets
python3 -m pip install voila

# 安装nbextensions
python3 -m pip install jupyter_contrib_nbextensions

# 安装 javascript和css文件
jupyter contrib nbextension install --user

# 安装configurator
python3 -m pip install jupyter_nbextensions_configurator
