# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第092页 (PDF第102页)
# 上下文: Jupyter 需要通过pip 方式安装，可以参考如下代码完成主程序安装。 ／ JupyterLab 前需要先安装Node.js 和NPM。

# 准备pip安装
sudo apt install python3-pip -y
python3  -m pip install --upgrade pip

# 安装Jupyter及JupyterLab
sudo python3 -m pip install jupyter jupyterlab
