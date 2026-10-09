# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第102页 (PDF第112页)
# 上下文: 改本机用户权限。 ／ 这在操作上稍有不便，可以通过配置Docker 组权限的方式进行改进，参考以下命令修

# 初始化Docker 用户配置

# 新增Docker组
sudo groupadd docker
# 将本机用户增设至Docker组中
sudo usermod -aG docker $USER
