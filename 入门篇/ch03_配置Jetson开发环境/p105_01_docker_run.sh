# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第105页 (PDF第115页)
# 上下文: 下命令，构建名为“portainer”的Docker 容器，用于管理Docker 环境。 ／ 以命令方式管理Docker 环境在操作上有些不便，可以使用Port

docker run \
    -d \
    -p 9000:9000 \
    --name portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data portainer/portainer-ce
