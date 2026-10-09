# 《NVIDIA Jetson AI硬件开发实战：入门篇》代码提取索引

共 248 个代码块。文件名格式: `p页码_序号_标识.扩展名`。

## ch02_配置Jetson系统环境

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p020_01_dpkg_sdkmanager_210-11669_amd64.sh` | 020 | Shell | 用如下命令安装下载好的安装包sdkmanager_2.1.0-11669_amd64.deb。 ／ 这里以Ubuntu 20.04 的x86 主机烧录Jetso |
| `p020_02_apt_install.sh` | 020 | Shell | 这时，执行如下命令修复安装即可： ／ 图2-2 SDK Manager 常见安装错误 |
| `p020_03_sdkmanager.sh` | 020 | Shell | 完成安装后，直接执行如下命令即可打开SDK Manager： ／ 通常执行上述命令后，SDK Manager 即可正常安装完毕，如图2-3 所示。 |
| `p026_01_ifconfig.sh` | 026 | Shell | 进入系统桌面并连好网线或配置好Wi-Fi 后，可以通过如下命令获取设备IP 地址。 ／ Wi-Fi 连接好。Jetson Orin Nano 系统桌面如图2-1 |
| `p033_01_cd_extlinux.sh` | 033 | Shell | 手动修改引导信息。 ／ 拟机）上。右击U 盘根目录的空白处，在弹出的菜单中选择“打开终端”，执行以下命令并 |
| `p034_01_apt_update.sh` | 034 | Shell | 命令： ／ 如果在Jetson 设备上已经安装好了系统，仅仅想要升级JetPack 版本，可以参考如下 |
| `p035_01_apt_update.sh` | 035 | Shell | 以下命令更新软件源。 ／ Ubuntu 系统版本有所不同，因此推荐使用默认源。请读者在Jetson 系统首次开机后就执行 |
| `p036_01_apt_upgrade.sh` | 036 | Shell | Ubuntu 系统更新可以参考如下两个命令： |
| `p036_02_apt_purge.sh` | 036 | Shell | 若需将office、游戏等软件卸载，可以执行如下命令。 ／ 建议在完成上述系统更新任务后，卸载或清理不常用的软件。Jetson 设备储存空间有限， |
| `p036_03_apt_autoremove.sh` | 036 | Shell | 完成系统更新后，可以执行以下命令清理过期软件。 ／ 若需将office、游戏等软件卸载，可以执行如下命令。 |
| `p037_01_apt_install.sh` | 037 | Shell | 建议为Python 3 安装必要的组件包，可以参考如下命令。 |
| `p037_02_python3_pip.sh` | 037 | Shell | 进行升级，可参考如下命令。 ／ Linux 环境下很多软件的安装都会用到Python3-pip，在使用pip 安装软件前，应先对其 |
| `p038_01_rm_python.sh` | 038 | Shell | 下面，执行如下命令，将“python”命令由指向Python 2.7 改为指向Python 3.8。 ／ 图2-28 修正软链接前的Python 2 和Pyth |
| `p040_01_pip3.sh` | 040 | Shell | 可以使用如下命令安装JTOP，如果提示缺少pip，请参考2.2 节的内容完善Python 环境。 |
| `p040_02_pip3_install.sh` | 040 | Shell | 参考如下命令指定软件版本来安装JTOP。 ／ JTOP 版本较高。为适配JetPack，需要指定一个合适的JTOP 版本。JetPack 5.1.1 版本可以 |
| `p040_03_jtop.sh` | 040 | Shell | 安装好JTOP 后，注销或重启系统后可以通过如下命令启动JTOP。 ／ 参考如下命令指定软件版本来安装JTOP。 |
| `p041_01_add-apt-repository_ppa.sh` | 041 | Shell | 请参考如下命令安装Indicator Sysmonitor。 ／ Indicator Sysmonitor 位于第三方软件仓库，需要手动将其加入系统软件仓库中。 |
| `p041_02_indicator-sysmonitor.sh` | 041 | Shell | 后台启动Indicator Sysmonitor。 ／ 若上述安装过程无异常，则可使用如下命令 |
| `p042_01_cpu.txt` | 042 | 文本 | 可以对图2-34 所示的Sensors 中的参数进行定制化配置，以下配置项命令供参考。 ／ 图2-34 Indicator Sysmonitor 配置页用户定制 |
| `p043_01_fallocate_4G.sh` | 043 | Shell | 命令参考如下。 ／ 这里以Jetson Orin Nano 4GB 设备为例，需要为其设置大小为4GB 的交换空间，具体 |
| `p043_02_swapon.sh` | 043 | Shell | 完成上述操作后可使用如下命令查看当前的交换空间： ／ 命令参考如下。 |
| `p043_03_swapoff_swapfile.sh` | 043 | Shell | 如果需要删除交换空间，可以执行如下命令： ／ 以Jetson Orin Nano 为例，创建交换空间操作过程如图2-36 所示。 |
| `p045_01_add-apt-repository_ppa.sh` | 045 | Shell | 可以使用如下命令完成安装Terminator。 ／ 端，方便同时执行多个命令。 |
| `p045_02_gsettings_set.sh` | 045 | Shell | Terminator，可以执行如下命令。 ／ Ubuntu 系统可以使用快捷键<Ctrl+Alt+T> 开启默认终端，如果想要使用该快捷键打开 |
| `p045_03_gsettings_reset.sh` | 045 | Shell | 如果想要将设置回退到Ubuntu 默认设置，可以执行如下命令。 ／ Terminator，可以执行如下命令。 |
| `p047_01_lsblk.sh` | 047 | Shell | 使用如下命令对比查看新插入的存储设备信息。 ／ 以将Jetson 设备存储卡通过读卡器或硬盘盒接入主机，再通过脚本执行备份。 |
| `p047_02.sh` | 047 | Shell | 示。 ／ 现在，我们来构建Jetson 系统备份脚本，然后对存储设备进行备份，脚本内容如下所 |
| `p48-49_01_将这个脚本命名为Jetson_Backup.sh` | 48-49 | Shell | 图2-41 使用lsblk 命令查看存储设备信息 |
| `p049_01_将这个脚本命名为Jetson_Backup.sh` | 049 | Shell | 将这个脚本命名为Jetson_Backup.sh，并使用如下命令赋予执行权限。 |
| `p049_02_使用Jetson_Backup.sh` | 049 | Shell | 现在，通过如下命令执行系统备份。 ／ 图2-42 为备份脚本赋予执行权限 |
| `p050_01_在Jetson_Backup.sh` | 050 | Shell | 在Jetson_Backup.sh 的基础上稍作修改，构建Jetson 镜像恢复脚本，可参考如下内容。 ／ 1. 命令方式恢复Jetson 系统 |
| `p050_02_将这个脚本命名为Jetson_Recover.sh` | 050 | Shell | 将这个脚本命名为Jetson_Recover.sh，并使用如下命令赋予执行权限。 ／ 在Jetson_Backup.sh 的基础上稍作修改，构建Jetson 镜 |
| `p051_01_apt_install.sh` | 051 | Shell | 容。这里需要用到GParted 软件，可以通过如下命令进行安装。 ／ 在将镜像烧录到新设备后，并不会完全利用全部的存储空间，需要手动对存储设备扩 |
| `p052_01_sudo_gparted.sh` | 052 | Shell | 如下命令： |
| `p056_01_ssh_jetson.sh` | 056 | Shell | 用终端登录Jetson，参考如下命令。 ／ 知道Jetson 设备账号（如jetson）和IP 地址（如192.168.0.30）后，可在任意主机上使 |
| `p058_01_apt_install.sh` | 058 | Shell |  |
| `p058_02_cd.sh` | 058 | Shell | 我们可以在用户主目录下执行以下命令创建自启动服务。 ／ 单击图2-57 所示的“Screen Sharing”无法正常使用是因为未能打开Vino 的使能开关， |
| `p058_03_gsettings_set.sh` | 058 | Shell | 执行以下命令来配置VNC 服务，使其能打开桌面共享。 ／ （3）配置VNC 服务 |
| `p059_01_orggnomeVinogschema.xml` | 059 | XML | 需要将以下内容写入/usr/share/glib-2.0/schemas/org.gnome.Vino.gschema.xml 文件中。 ／ （4）配置VNC  |
| `p059_02_orggnomeVinogschema.sh` | 059 | Shell | 首先，执行如下命令，手动将上述内容插入<\schema> 节点前。 ／ 需要将以下内容写入/usr/share/glib-2.0/schemas/org.gno |
| `p060_01_orggnomeVinogschema.sh` | 060 | Shell | 然后，保存/usr/share/glib-2.0/schemas/org.gnome.Vino.gschema.xml 文件，开始编译。 |
| `p060_02_gsettings_set.sh` | 060 | Shell | 接着，执行以下命令就可以开启VNC 服务了。 ／ 储在相应的缓存文件中。 |
| `p060_03.sh` | 060 | Shell | 便于构建无人值守的批量操作脚本。 ／ 以通过执行如下脚本，在终端完成命令设置，这样 |
| `p060_04_PASSWORD.sh` | 060 | Shell | ####################################图2-59 Ubuntu 20.04 远程桌面配置 ／ 便于构建无人值守的批量操作脚本。 |
| `p061_01_mkdir.sh` | 061 | Shell | 为了使Vino 服务在每次开机时都能使用，可以执行如下命令，创建桌面自启动脚本。 |
| `p061_02_vino-server.desktop` | 061 | desktop | 准备好以下自启动脚本内容。 ／ 为了使Vino 服务在每次开机时都能使用，可以执行如下命令，创建桌面自启动脚本。 |
| `p061_03_vino-server.sh` | 061 | Shell | 通过如下命令，将上述内容输入或粘贴至~/.config/autostart/vino-server.desktop 文件中。 ／ 准备好以下自启动脚本内容。 |
| `p062_01_dpkg_nomachine_8113_3_arm64deb.sh` | 062 | Shell | 录并执行以下命令完成NoMachine 安装。 ／ 这里以下载nomachine_8.11.3_3_arm64.deb 安装包为例，完成下载后，切换到下载目 |
| `p066_01_xrandr_1024.sh` | 066 | Shell | 可以参考如下命令，验证并设置初始屏幕分辨率。 ／ 使用Jetson 设备时，接入的显示器屏幕尺寸得设置过大可能会导致Jetson 设备过载。 |
| `p066_02_mkdir.sh` | 066 | Shell | 为了使系统每次都能保持同样的屏幕尺寸，可以进行如下操作。 ／ 可以参考如下命令，验证并设置初始屏幕分辨率。 |
| `p066_03_Type.desktop` | 066 | desktop | 接着，创建一个自启动文件，屏幕尺寸配置为“1024×600”，内容如下。 ／ 为了使系统每次都能保持同样的屏幕尺寸，可以进行如下操作。 |
| `p066_04_vim.sh` | 066 | Shell | 执行以下命令并将上述内容贴入文件中。 ／ 接着，创建一个自启动文件，屏幕尺寸配置为“1024×600”，内容如下。 |
## ch03_配置Jetson开发环境

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p074_01_apt-get_update.sh` | 074 | Shell |  |
| `p075_01_cd_tmp.sh` | 075 | Shell | 具体执行过程参考以下命令。 ／ 在“ /tmp”目录下构建编译目录，并用git 获取OpenCV 和OpenCV-Contrib 两个包， |
| `p75-76_01_cd_opencv.sh` | 75-76 | Shell | 自行调整相关参数（CUDA_ARCH 和CUDNN_VERSION）。 ／ Jetson Orin Nano 设备编译OpenCV 命令如下，其他Jetson  |
| `p076_01_make.sh` | 076 | Shell | makefile 编译成功后，建议关闭其他程序，使用CPU 全核编译。 ／ OpenCV 版本。 |
| `p077_01_sudo_ldconfig.sh` | 077 | Shell | 通过编译安装的OpenCV 通常需要手动加载“.so”文件，可以按照如下命令手动加载。 ／ Python 正常运行。 |
| `p078_01_source.sh` | 078 | Shell |  |
| `p078_02_echo.sh` | 078 | Shell | 可以通过如下命令查看当前OpenCV C++ 版本。 ／ 要遗漏。 |
| `p078_03_opencv_version.sh` | 078 | Shell | 下命令。 ／ 如果需要查看OpenCV 当前版本的详细信息，如Python 版本安装路径等，可以执行如 |
| `p078_04_python3.sh` | 078 | Shell | 或者使用Python 程序查看OpenCV 编译详情。 ／ 下命令。 |
| `p079_01_mkdir.sh` | 079 | Shell | METADATA 元数据信息文件。 ／ 读者可以参考如下代码构建OpenCV-Python METADATA 和OpenCV-Contrib-Python。 |
| `p080_01_opencv_cuda_check.cpp` | 080 | C++ | 加速是否可用，具体内容如下。 ／ 构建一个名为“ opencv_cuda_check.cpp”的C++ 文件，用于检测OpenCV 使用GPU |
| `p080_02_g.sh` | 080 | Shell | 细信息，验证OpenCV 可以使用GPU 加速。 ／ 然后，编译并执行测试操作，可参考以下命令对上述代码进行编译，获得GPU 设备详 |
| `p081_01_opencv_cuda_check.sh` | 081 | Shell | 通过下面的命令运行编译后的执行文件（opencv_cuda_check）。 |
| `p082_01_python3.sh` | 082 | Shell | 下面验证 OpenCV Python 版本是否支持GPU 加速，参考如下命令进行简要测试。 ／ （2）OpenCV Python 版本测试 |
| `p082_02_import.py` | 082 | Python | 可以通过如下代码来查看GPU 设备详情： ／ 图3-8OpenCV 开启GPU 加速（Python 版本测试） |
| `p083_01_apt_install.sh` | 083 | Shell | 在安装TensorFlow 前对现有Python 环境依赖包版本做如下处理。 ／ 1. 安装TensorFlow |
| `p084_01_cd.sh` | 084 | Shell | 完成h5py 编译后，TensorFlow 安装就没有任何悬念了，参考以下命令执行安装即可。 |
| `p084_02_python3.sh` | 084 | Shell | 通过执行以下代码来测试GPU 是否可用。 ／ 2. 测试TensorFlow |
| `p84-85_01_import.py` | 84-85 | Python | 自动识别GPU 并使用GPU 运算。 ／ 会尽可能智能地在可用的CPU 和GPU 之间分配操作。可以通过如下代码测试其是否能够 |
| `p086_01_apt_install.sh` | 086 | Shell | 安装PyTorch 可参考如下命令。 ／ （1）安装PyTorch |
| `p087_01_apt_install.sh` | 087 | Shell | 安装TorchVision 时注意与PyTorch 版本匹配，可参考如下命令完成手动编译安装。 ／ 图3-12TorchVision 包引用警告 |
| `p087_02_python3_setuppy.sh` | 087 | Shell | TorchVision 打包成“*.whl”文件，便于日后使用。 ／ TorchVision 编译过程需要花费一些时间，请读者耐心等待。也可以使用如下命令将 |
| `p088_01_apt_update.sh` | 088 | Shell |  |
| `p088_02_CMake_Error.txt` | 088 | 终端输出 | 在具体编译时，可能会遇到CMake 版本过低而导致无法编译的问题，具体如下。 |
| `p088_03_wget_https.sh` | 088 | Shell | 这种情况，可以使用如下命令升级CMake 版本。 ／ 在具体编译时，可能会遇到CMake 版本过低而导致无法编译的问题，具体如下。 |
| `p088_04_cmake.sh` | 088 | Shell | 接着，验证CMake 版本。 ／ 这种情况，可以使用如下命令升级CMake 版本。 |
| `p88-89_01_git_clone.sh` | 88-89 | Shell | 编译。 ／ 如果版本符合编译环境要求，可以参考TorchVision 的编译过程来完成TorchAudio 的 |
| `p089_01_python3.sh` | 089 | Shell | 执行以下代码测试PyTorch 是否支持GPU 加速。 ／ 2. 测试PyTorch |
| `p089_02_import.py` | 089 | Python | 下面测试PyTorch，使其在GPU 上完成操作，可参考如下代码。 ／ 图3-13PyTorch 验证GPU 加速是否可用 |
| `p092_01_前需要先安装Node.sh` | 092 | Shell | JupyterLab 前需要先安装Node.js 和NPM。 ／ Package Manager, Node 包管理器）是Node.js 生态系统中不可或缺的一 |
| `p092_02_前需要先安装Node.sh` | 092 | Shell | Jupyter 需要通过pip 方式安装，可以参考如下代码完成主程序安装。 ／ JupyterLab 前需要先安装Node.js 和NPM。 |
| `p093_01_python3_pip.sh` | 093 | Shell |  |
| `p093_02_python3_pip.sh` | 093 | Shell | 当然，也有中文语言包插件，可执行如下命令安装。 |
| `p093_03_jupyter_notebook.sh` | 093 | Shell | 执行以下命令。 ／ 完成插件安装后，需要为Jupyter 设置密码，以便对远程控制Jetson 设备进行管理，可 |
| `p093_04_jupyter_lab.sh` | 093 | Shell | 现在执行以下命令，启动JupyterLab。 ／ 图3-16Jupyter 密码设定 |
| `p94-95_01_将上述内容粘贴到jupyter.desktop` | 94-95 | desktop | 件，可参考如下命令。 ／ 为了能让Jupyter 服务在每次登录系统后都能直接访问，可以构建一个自启动桌面文 |
| `p095_01_将上述内容粘贴到jupyter.sh` | 095 | Shell | 执行以下代码，将上述内容粘贴到jupyter.desktop 文件中。 |
| `p102_01_groupadd_docker.sh` | 102 | Shell | 改本机用户权限。 ／ 这在操作上稍有不便，可以通过配置Docker 组权限的方式进行改进，参考以下命令修 |
| `p103_01_docker_run.sh` | 103 | Shell | 会自行拉取最新版本的镜像文件。 ／ 参考以下命令，使用“ docker run”运行hello-world，如果尚未拉取该镜像，Docker |
| `p103_02_docker_run.sh` | 103 | Shell | 令行。 ／ 如图3-26 示例，可以使用如下命令运行最新版本的Ubuntu 操作系统，并同时进入命 |
| `p103_03_cat_os-release.sh` | 103 | Shell | 进入Ubuntu 系统后，执行以下命令查看当前系统版本。 ／ 令行。 |
| `p104_01_docker_images.sh` | 104 | Shell | 容器。 ／ 使用Docker 相关命令可以管理镜像或容器，可使用以下命令查看镜像和运行中的 |
| `p105_01_docker_run.sh` | 105 | Shell | 下命令，构建名为“portainer”的Docker 容器，用于管理Docker 环境。 ／ 以命令方式管理Docker 环境在操作上有些不便，可以使用Port |
| `p107-108_01_Dockerfile` | 107-108 | Dockerfile | 的软件，读者可根据自身需要进行调整。 ／ 这个过程主要限定了基础镜像来源，禁用了系统交互界面，并预先安装了镜像中用到 |
| `p108-109_01_Dockerfile` | 108-109 | Dockerfile | foxy/Installation.html。 ／ 在这个部分完成Foxy 安装的全部过程，相关命令参考ROS 官网https://docs.ros.org/e |
| `p109_01_Dockerfile` | 109 | Dockerfile | 以使用“ros2”命令。 ／ 这一部分完成ROS 环境的最终配置与初始化，并激活ROS 环境，以便在Docker 中可 |
| `p109_02_docker_build.sh` | 109 | Shell | 上述内容已完成Dockerfile 构建，现在执行编译工作，参考如下命令。 ／ 以使用“ros2”命令。 |
| `p110_01_xhost.sh` | 110 | Shell | 一个图形化测试，具体脚本内容如下。 ／ 下面，编写支持Docker 容器图形化界面操作的运行命令，并使用ROS 海龟仿真器做 |
| `p111_01_docker_exec.sh` | 111 | Shell | 执行上述脚本，启动Docker 容器，然后在另一个命令窗口执行以下命令，进入该容器。 ／ 使用Docker 的其他安全特性。 |
| `p111_02_ros2_run.sh` | 111 | Shell | 海龟仿真器。 ／ 现在使用ROS 海龟仿真器演示图形化操作，在第一个命令行窗口输入以下命令，启动 |
| `p111-112_01_ros2_run.sh` | 111-112 | Shell | 在另一个命令行窗口，启用键盘控制，参考如下命令。 ／ 互操作。 |
## ch04_使用Jetson看世界

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p116_01_ll_video.sh` | 116 | Shell | 连接好CSI 摄像头后，我们可以使用如下命令查询是否能正常识别该设备。 ／ 意 |
| `p117_01_apt-get_update.sh` | 117 | Shell | 我们先来安装V4L2 命令行工具（v4l2-ctl），它位于v4l-utils 包中，参考执行以下命令。 ／ 务的实现。 |
| `p117_02_v4l2-ctl.sh` | 117 | Shell | 使用如下命令查看视频设备列表。 ／ 1. 查看视频设备列表 |
| `p118_01_v4l2-ctl_video2.sh` | 118 | Shell | 使用如下命令查看视频设备所支持的格式。 ／ 2. 查看视频设备支持的视频格式 |
| `p119_01_ffmpeg_v4l2.sh` | 119 | Shell | 使用FFmpeg 等工具测试视频设备，确保它可以正常工作，可参考如下命令。 ／ 3. 测试视频设备 |
| `p121_01_gst-launch-10_v4l2src.sh` | 121 | Shell | 下命令调用USB 摄像头。 ／ 有了gst-launch-1.0，调用USB 摄像头获取画面就要比前文的操作简便多了，可参考如 |
| `p121-122_01_nvgstcapture-10.sh` | 121-122 | Shell | 面，可以使用如下命令。 ／ 如果仅仅是想要简便地调用CSI 摄像头设备，在显示器画面中查看摄像头捕获到的画 |
| `p122_01_git_clone.sh` | 122 | Shell | 执行以下命令，克隆JetCam，并执行安装动作。 ／ 1. 安装JetCam |
| `p122_02_usb_camera.txt` | 122 | 文本 | 考构建自己的实现。 ／ 可以在“ usb_camera.py”中查看这个函数，以此作为参 |
| `p122_03_def__gst_str.py` | 122 | Python | 图4-8JetCam 文件结构 ／ 考构建自己的实现。 |
| `p123_01_from.py` | 123 | Python | 首先，引入JetCam 库，并初始化摄像头对象。 ／ “jetcam/notebooks/usb_camera/usb_camera.ipynb”文件，逐步操作 |
| `p123_02_image.py` | 123 | Python | 现在获取摄像头画面，并使用widget 将其展现在JupyterLab 中。 ／ 设定摄像头画面为640×480 像素。 |
| `p123-124_01_camerarunning.py` | 123-124 | Python | 这时的画面只有一帧，所以是静态画面，可以参考如下代码使画面实时展现。 ／ 现在获取摄像头画面，并使用widget 将其展现在JupyterLab 中。 |
| `p124_01_的csi_camera.py` | 124 | Python | 实现。 ／ 如果想要在Python 代码中调用CSI 摄像头设备，可以参考JetCam 的csi_camera.py 的 |
| `p125_01_from.py` | 125 | Python | 引入JetCam 操作CSI 摄像头的库，并初始化CSI 摄像头。 ／ 以参考“jetcam/notebooks/csi_camera/csi_camera.i |
| `p125_02_camera0.py` | 125 | Python | 或者同时初始化2 个CSI 摄像头设备，可以参考如下代码。 ／ 这里默认对“ /dev/video0”设备进行初始化。如果想要初始化其他CSI 摄像头设备， |
| `p125-126_01_import.py` | 125-126 | Python | 对象，并为摄像头设置分辨率和帧率。 ／ 在引入OpenCV 库后，构建open_usb_camera 这个函数，在函数内创建 VideoCapture |
| `p126_01_def_capture_usb_frames.py` | 126 | Python | 接下来，构建capture_usb_frames 函数，从摄像头逐帧读取，并将其画面展示出来。 |
| `p126_02_usb_camera.py` | 126 | Python | 最后，以此调用上述两个函数，调用USB 摄像头。 ／ 接下来，构建capture_usb_frames 函数，从摄像头逐帧读取，并将其画面展示出来。 |
| `p126-127_01_import.py` | 126-127 | Python | 数中完成命令字构建，并初始化CSI 摄像头。 ／ 使用OpenCV 操作CSI 摄像头，需要借助GStreamer 管道命令，在open_csi_camera  |
| `p127_01_def_capture_csi_frames.py` | 127 | Python | 接下来，构建capture_csi_frames 函数，用于展示CSI 摄像头获得视频数据。 ／ VideoCapture 对象时与USB 摄像头有所不同，使用 |
| `p127_02_csi_camera.py` | 127 | Python | 最后，依次调用上述两个函数，完成CSI 摄像头调用。 ／ 接下来，构建capture_csi_frames 函数，用于展示CSI 摄像头获得视频数据。 |
| `p128_01_gst-launch-10_v4l2src.sh` | 128 | Shell | 格式并通过网络传输。 ／ USB 摄像头需要使用V4L2，然后使用rtph264pay 将来自 USB 摄像头的数据流打包为RTP |
| `p129_01_gst-launch-10_nvarguscamerasrc.sh` | 129 | Shell |  |
| `p129_02_gst-launch-10_udpsrc.sh` | 129 | Shell | 最后，我们在另一个终端中接受RTP 服务，并将视频数据呈现在桌面。 ／ 上述CSI 摄像头RTP 服务命令字参数与USB 摄像头部分别无二致，这里不再复述。 |
| `p129_03_gst-launch-10_v4l2src.sh` | 129 | Shell | 首先，为USB 摄像头构建一个RTSP 实时视频流服务。 ／ 2. 基于RTSP 构建实时视频流服务 |
| `p130_01_gst-launch-10_nvarguscamerasrc.sh` | 130 | Shell | 接下来，如法炮制，为CSI 摄像头构建RTSP 服务。 ／ 迟处理。 |
| `p130_02_gst-launch-10_udpsrc.sh` | 130 | Shell | 最后，我们在另一个终端中接受RTSP 服务，并将视频数据渲染。 ／ 上述命令关键参数与USB 摄像头RTSP 服务基本一致，这里不再复述。 |
| `p135_01_pip_torch.sh` | 135 | Shell | 成开发环境搭建，以下命令供参考。 ／ PyTorch、TorchVision 和NumPy 在本书第三章中已有介绍，读者可以参考章节内容完 |
| `p135_02_import.py` | 135 | Python | 这里导入用于模型构建相关的库。 ／ 2. 导入必要的库 |
| `p136_01_device.py` | 136 | Python | 代码启用GPU 设备。 ／ 按照第3 章内容完成开发环境配置后，使用PyTorch 时可以开启GPU 加速，执行如下 |
| `p136-137_01_transform.py` | 136-137 | Python | 过以下代码构建训练数据集和测试数据集。 ／ PyTorch 和 TensorFlow 都内置了 MNIST 数据集，方便用户进行实验和测试。可以通 |
| `p137_01_class_DNN.py` | 137 | Python | 在这个实例中，使用了多层神经网络DNN，共构建了3 个隐藏层，并使用GPU 加速。 ／ 5. 定义神经网络模型 |
| `p137_02_pip_install.sh` | 137 | Shell | 调试、优化和文档编制特别有用，使得模型的设计和实现更加透明。 ／ 参数，并返回一个清晰的表格，显示模型的每一层、输出形状、参数量和计算量。这对于 |
| `p138_01_from.py` | 138 | Python | 现在执行以下代码查看网络模型信息。 |
| `p139_01_criterion.py` | 139 | Python | 使得模型的预测结果更加准确。 |
| `p139_02_nettrain.py` | 139 | Python | 现在使用GPU 训练模型，共训练10 个epoch（训练轮数）。 ／ 7. 训练模型 |
| `p140_01.txt` | 140 | 终端输出 | 高。这是正常现象，因为模型的参数在初始时是随机的，需要通过训练逐步调整。 ／ 查看日志可知损失（loss）最初比较大，这表明模型在初始阶段尚未充分学习，损失较 |
| `p140_02_torchsave.py` | 140 | Python | 将模型保存下来以便后续使用，可参考如下代码。 ／ 8. 保存模型 |
| `p140-141_01_model_weights_path.py` | 140-141 | Python | 经过上述过程，我们已经获得了模型，下面进行评估。 ／ 9. 评估模型 |
| `p141_01_Accuracy_of.txt` | 141 | 文本 | 上述代码执行结果如下： |
| `p141_02_classification_rep.py` | 141 | Python | 执行以下代码，评估模型性能。 ／ 说明模型在测试集上表现非常好，具有较强的分类能力。 |
| `p141-142_01_precision_recall.txt` | 141-142 | 终端输出 | 较为成功，模型泛化能力较好。 ／ 能力。模型在不同类别上的表现相对均衡，没有明显地过度偏向某个类别，说明训练过程 |
| `p142-143_01_def_imshow.py` | 142-143 | Python | 像直接展示出来。 ／ 为了更直观地对比正误图像分类结果，可以使用如下方法将正确分类和错误分类的图 |
| `p144-145_01_kagglecatsanddogs_5340.py` | 144-145 | Python | 据集。 ／ 我们使用如下代码下载“ kagglecatsanddogs_5340.zip”并将其解压，准备猫狗分类数 |
| `p145-146_01_import.py` | 145-146 | Python | 下代码完成数据预处理。 ／ 理。同时，需要将图片数据分组，一部分用于训练，另一部分用于验证。本实例将使用如 |
| `p146-147_01_import.py` | 146-147 | Python | ResNet-34 模型。读者可以参考4.3.1 节中的模型代码示例，来查看当前模型结构。 ／ 现在来定义神经网络模型，这里使用了ResNet-18 模型。在这 |
| `p147_01_criterion.py` | 147 | Python | 优化性能。 ／ 和优化器（optimizer）是关键组件，它们分别负责衡量模型预测的准确性和更新模型参数以 |
| `p147-148_01_num_epochs.py` | 147-148 | Python | 我们将训练轮数（epoch）设为10 次，并尽可能在GPU 上完成训练。 ／ 3. 训练模型 |
| `p148_01_Epoch_10.txt` | 148 | 终端输出 | 距的指标。损失值越低，说明模型的预测结果越接近实际标签。 ／ 上述代码中，我们需要关注的是损失值（Loss），它是衡量模型预测与实际标签之间差 |
| `p148_02_model_path.py` | 148 | Python | 可将该模型保存下来，以便后续使用。 ／ 上述代码执行结果损失值降到了0.0020，说明模型在训练数据上的表现已经非常出色。 |
| `p148-149_01_model_path.py` | 148-149 | Python | 加载刚才保存好的模型，开启评估模式。 ／ 5. 评估模型 |
| `p149_01_Validation_Accuracy.txt` | 149 | 文本 | 上述代码模型准确率输出结果如下： |
| `p149-150_01_import.py` | 149-150 | Python | 先来构建用于展示图片的函数，对图片进行裁剪。 ／ 最后，来对结果进行一个抽样，验证模型训练效果。 |
| `p150_01_def_group_predictions.py` | 150 | Python | 下面根据预测结果和实际情况对图片进行分组处理。 |
| `p151_01_def_plot_prediction_collection.py` | 151 | Python | 最后，构建一个函数用于图片展示。 |
| `p151_02_class_names.py` | 151 | Python | 现在，执行正误图片展示。 ／ 最后，构建一个函数用于图片展示。 |
| `p152_01_import.py` | 152 | Python | 首先加载模型，参考如下代码。 ／ 图4-15猫狗分类（ResNet）正误预测图片集 |
| `p152-153_01_onnx_path.py` | 152-153 | Python | 接下来将“resnet_cat_dog_classifier.pth”转换为“resnet_cat_dog_model.onnx”。 ／ 首先加载模型，参考如下 |
| `p153_01_labels.sh` | 153 | Shell | onnx”。同时，还需要构建标签文件“labels.txt”，并在文件中写入以下两行内容。 ／ 现在，我们就获得了ONNX 格式的猫狗图片分类模型文件“ res |
## ch05_Jetson-Inference项目

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p155_01_apt_update.sh` | 155 | Shell | 步骤1准备编译工具。为顺利完成后续编译，请执行以下命令安装必要的编译工具。 ／ 完成。 |
| `p156_01_git_clone.sh` | 156 | Shell | Cmake。 ／ 步骤2克隆并配置Cmake。切换到用户主目录下，克隆Jetson-Inference，并配置 |
| `p156_02_cd_jetson-inference.sh` | 156 | Shell | 如果编译过程出现异常，请执行以下命令。 ／ Cmake。 |
| `p157_01_cd_build.sh` | 157 | Shell | 在这个环节中，可以直接选择“Skip”跳过安装，之后执行以下命令重新选择。 |
| `p157_02_make.sh` | 157 | Shell | 步骤３编译安装。现在可以执行编译操作，完成安装任务了。 ／ 在这个环节中，可以直接选择“Skip”跳过安装，之后执行以下命令重新选择。 |
| `p157_03_cd_tools.sh` | 157 | Shell | 载好。执行以下命令，完成模型下载。 ／ 步骤4下载模型。为了节约后续的准备时间，现在可以把后续任务用到的模型提前下 |
| `p158_01_run.sh` | 158 | Shell | 由于运行容器需要各种挂载和设备，建议使用脚本“docker/run.sh”来运行容器。 |
| `p160_01_COMMAND_input_URI.txt` | 160 | 文本 | Jetson-Inference 提供的命令行操作参数格式比较统一，如下所示。 ／ 试模型的推理功能，确保模型正确运行。 |
| `p161_01_cd_jetson-inference.sh` | 161 | Shell | 在正式使用Jetson-Inference 前，可以使用工具检查摄像头。 ／ 建一个 OpenGL 显示窗口，除非指定了 --headless 参数。 |
| `p161_02_cd_jetson-inference.sh` | 161 | Shell | 也可以将摄像头获得的视频数据进行存储。 ／ 这时，Jetson-Inference 会调起对应的摄像头，并在显示器上输出画面。 |
| `p163_01_cd_bin.sh` | 163 | Shell | 可以使用如下命令调用摄像头进行图像分类，并将结果输出到显示器上。 ／  --topK：可选，用于显示分类预测的前 K 个结果（默认为1 个）。 |
| `p164_01_cd_bin.sh` | 164 | Shell | AlexNet 网络模型等，如下文命令所示。 ／ 除了使用默认摄像头数据和默认网络模型，也可以使用RTSP 流作为输入源，或使用 |
| `p165_01_import.py` | 165 | Python | 首先，在文件顶部添加一个shebang 注释，并导入需要使用到的Python 模块。 |
| `p165_02_warning.txt` | 165 | 终端输出 | 如果收到了如下提示，请注意是否使用了正确的Python 模块。 ／ 令行的标准包。 |
| `p165_03_parser.py` | 165 | Python | 接下来对参数进行解析，并为网络参数设置默认值。 ／ jetson_utils。 |
| `p165_04_img.py` | 165 | Python | 现在，加载图像文件以及网络。 ／ 接下来对参数进行解析，并为网络参数设置默认值。 |
| `p165_05_class_idx.py` | 165 | Python | 行分类，并将结果输出。 ／ 也可以在执行命令时，根据表5-4 所示使用其他预训练网络模型。接下来，对图像进 |
| `p166_01_chmod.sh` | 166 | Shell | 现在，为上述Python 文件添加执行权限。 |
| `p166_02_my-recognition1py_dog_2jpg.sh` | 166 | Shell | 执行以下命令，使用Jetson-Inference 自带的图片库进行图像分类推理。 ／ 现在，为上述Python 文件添加执行权限。 |
| `p166_03_image_is.txt` | 166 | 终端输出 | 一辙。 ／ 的置信度为 99.80%，表示模型对这个分类结果非常确定，这和我们肉眼判断的结果如出 |
| `p169_01_cd_bin.sh` | 169 | Shell | 使用以下命令调用Jetson-Inference 做目标检测推理。 ／ 示例1物体识别 |
| `p170_01_cd_bin.sh` | 170 | Shell | Jetson-Inference 自带的图片库进行人脸检测，并将结果标记在图片上。 ／ 我们先来使用专门进行人脸识别任务的模型—TAO FaceDetect。执 |
| `p170_02_cd_bin.sh` | 170 | Shell | PeopleNet 对比测试，参考以下命令更换网络模型。 ／ 这显然不符合我们的预期，TAO FaceDetect 模型对于侧脸识别不尽如人意，改用TAO |
| `p171_01_cd_bin.sh` | 171 | Shell |  --labels：可选，标签，与自定义模型相对应。 ／  --model：可选，自定义模型，支持caffemodel、UFF 和ONNX 模型。 |
| `p171_02_detectnet1.py` | 171 | Python | 首先，加载需要的Python 模块。 ／ detectnet1.py”的Python 实现。 |
| `p171_03_net.py` | 171 | Python | 接下来，配置网络模型和输入输出流。 ／ 因为直接指定了摄像头作为图像输入源，所以这里省去了参数获取实现。 |
| `p172_01_while_displayIsStreaming.py` | 172 | Python |  |
| `p172_02_chmod.sh` | 172 | Shell | 现在，为该文件赋予执行权限，并执行该文件。 |
| `p175_01_cd_bin.sh` | 175 | Shell | 使用以下命令调用Jetson-Inference 对多人图片做语义分割 推理。 ／  --filter-mode：可选，标志接受point 或linear 采 |
| `p178_01_cd_bin.sh` | 178 | Shell | 使用以下命令调用Jetson-Inference 对图片做身体姿态估计推理。 ／ 示例1身体姿态估计推理 |
| `p179_01_cd_bin.sh` | 179 | Shell | 参考以下命令，使用摄像头获取图像做手势姿态估计。 ／ 解手部的动态变化和静态姿势。 |
| `p182_01_cd_bin.sh` | 182 | Shell | 在Jetson-Inference 工作目录构建一个video 目录并建立软链接，方便我们后续操作。 ／ 过学习和探索新的真实动作类别来鼓励对动作识别的进一步研 |
| `p182_02_wget_https.sh` | 182 | Shell | 下载UCF101 数据集并解压缩，参考如下命令。 ／ 在Jetson-Inference 工作目录构建一个video 目录并建立软链接，方便我们后续操作。 |
| `p182_03_cd_ucf.sh` | 182 | Shell | 任选一个视频文件，使用FFmpeg 对其格式进行转换，参考以下命令。 ／ Jetson-Inference 支持的数据格式。 |
| `p183_01_cd_bin.sh` | 183 | Shell | 完成视频文件格式转换后，使用ActionNet 做动作识别推理，参考如下命令。 ／ 时数据。 |
| `p183_02_cd_bin.sh` | 183 | Shell | 当然，也可以直接开启摄像头，通过自身动作变化来进行动作识别推理。 ／ 帧视频呈现时Jetson-Inference 动作识别推理结果的变化。 |
| `p185_01_cd_bin.sh` | 185 | Shell | Jetson-Inference 提供的背景去除推理简单易用，参考如下命令，对图片背景进行替换。 ／  --replace：可选，替换背景图片。 |
| `p185_02_cd_bin.sh` | 185 | Shell | 现在将摄像头作为输入源，实时进行背景替换，参考如下命令。 ／ 处理，就可以完成背景去除，整个过程完全自动化。 |
| `p188_01_cd_bin.sh` | 188 | Shell | 执行以下命令，对图片进行单眼深度推理。 ／ inverted）。 |
## ch06_Jetson硬件控制基础

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p198_01_sudo_config-by-pinpy.sh` | 198 | Shell | GPIO 引脚的开闭状态前，通过以下命令查看GPIO 引脚状态。 ／ 烧录SDK 时已经预装到Jetson 设备中，如果无法正常使用，请参考前文。在正式配置 |
| `p199_01_config-by-pinpy_1.sh` | 199 | Shell | 如果只想要查看特定引脚，如引脚33 的配置是否生效，可以参考如下命令。 ／ 图6-10Jetson 系统GPIO 40 引脚状态 |
| `p200_01_sudo_jetson-iopy.sh` | 200 | Shell |  |
| `p203_01_config-by-pinpy_1.sh` | 203 | Shell | 生效。 ／ 状态，即开启了PWM 信号输出功能。可以通过以下命令检测引脚15 及其他引脚配置是否 |
| `p204_01_ls_kernel.sh` | 204 | Shell | 这时在Jetson 设备的“/boot”目录下可以获得用户自定义DTB 文件，检索命令如下。 ／ 图6-17Jetson 硬件接口配置—设备树生成提示界面 |
| `p204_02_extlinux.sh` | 204 | Shell | 中，参考以下命令查看该文件尾部配置。 ／ 文件，该文件在Jetson 设备启动时生效。相关配置在文件“ /boot/extlinux/extlinux.conf |
| `p204_03_LABEL_JetsonIO.cfg` | 204 | 配置 | 在该配置文件末尾可以见到以下内容。 ／ 中，参考以下命令查看该文件尾部配置。 |
| `p206_01_apt_reinstall.sh` | 206 | Shell |  |
| `p209_01_pip3_install.sh` | 209 | Shell | 有Jetson.GPIO 库，可以通过以下命令安装： |
| `p209_02_pip3_uninstall.sh` | 209 | Shell | 如果Jetson.GPIO 出现版本异常，可以卸载Jet son.GPIO 重新安装。 ／ 有Jetson.GPIO 库，可以通过以下命令安装： |
| `p209_03_git_clone.sh` | 209 | Shell | 或者，使用如下命令本地安装。 ／ 如果Jetson.GPIO 出现版本异常，可以卸载Jet son.GPIO 重新安装。 |
| `p209_04_import.py` | 209 | Python | 使用 GPIO。参考如下代码，将stderr 重定向到/dev/null 以屏蔽警告信息。 ／ 如果硬件可以正常工作，并且确定不需要修复该警告，则可以选择忽略该 |
| `p210_01_git_clone.sh` | 210 | Shell | 上编写自己的案例。这些示例代码可通过如下方式获取。 ／ NVIDIA 官方为Jetson 用户提供Jetson.GPIO 示例代码，我们可以在参考示例代码基础 |
| `p210_02_GPIOsetmode.py` | 210 | Python | 式，即物理引脚编号模式。 ／ GPIO 模式共有两种：BCM 模式和BOARD 模式。对于初学者，推荐使用BOARD 模 |
| `p210_03_GPIOsetmode.py` | 210 | Python | 上述代码将GPIO 设置为BOARD 模式，也可以将其设置为BCM 模式，参考如下代码。 ／ 式，即物理引脚编号模式。 |
| `p210_04_GPIOsetup.py` | 210 | Python | GPIO 引脚可以配置为输入/ 输出模式，使用 GPIO.setup() 来设置，参考如下代码。 ／ 2. GPIO 引脚输入/ 输出模式 |
| `p211_01_state.py` | 211 | Python | GPIO 引脚共有高、低两种状态，可以通过以下代码获取GPIO 引脚状态。 ／ 3. 读取引脚状态 |
| `p211_02_GPIO.py` | 211 | Python | 操作中出现冲突。 ／ 在程序结束时，需要调用 GPIO.cleanup() 来清理设置，释放 GPIO 引脚，防止在后续 |
| `p211_03_GPIOadd_event_detect.py` | 211 | Python | 化时触发。 ／ Jetson.GPIO 库提供了事件检测功能，我们可以设置一个回调函数，在引脚状态发生变 |
| `p212_01_import.py` | 212 | Python | 度等。使用 GPIO.PWM() 方法即可实现PWM 信号输出，完成上述控制。 ／ 号。例如，通过调节占空比，可以模拟出不同电压的平均值，用于控制电机转速、LE |
## ch07_JetsonGPIO应用实践

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p215-216_01_import.py` | 215-216 | Python | 式，并绑定GPIO 引脚地址。 ／ 我们先进行初始化，将GPIO 设置为BOARD 模式，将RGB 灯珠引脚设置为输出模 |
| `p216_01_def_light_color.py` | 216 | Python | 为方便同时控制3 个LED 亮/ 灭，在此构建一个函数。 |
| `p216_02_light_color.py` | 216 | Python | 通过000 →111 高低电平编码来控制单个LED 灯的亮灭。 ／ 为方便同时控制3 个LED 亮/ 灭，在此构建一个函数。 |
| `p216_03_GPIOcleanup.py` | 216 | Python | 最后一定要清理GPIO 设置，避免GPIO 引脚冲突。 ／ 通过000 →111 高低电平编码来控制单个LED 灯的亮灭。 |
| `p217-218_01_import.py` | 217-218 | Python | 在代码初始化部分将蜂鸣器控制引脚设置为高电平，以免误报。 ／ 2. 代码实现 |
| `p218_01_def_buzzer.py` | 218 | Python | 构建一个函数，通过循环触发蜂鸣器发出警报。 ／ 图7-4Jetson GPIO 控制RGB 灯珠+ 蜂鸣器 |
| `p218_02_buzzer.py` | 218 | Python | 最后，调用该函数，并清理GPIO 设置。 ／ 构建一个函数，通过循环触发蜂鸣器发出警报。 |
| `p220_01_TRIG.py` | 220 | Python | 图7-6Jetson GPIO 实现倒车雷达 ／ PIN1 |
| `p220-221_01_def_get_distance.py` | 220-221 | Python | 接下来，根据前文所述的测距公式来构建一个测距函数。 ／ 图7-6Jetson GPIO 实现倒车雷达 |
| `p221_01_if___name.py` | 221 | Python | 距离，亮红灯，并使用蜂鸣器报警，这将使用到前文部分代码。 ／ 我们期望，当距离大于15cm 时视为安全距离，亮绿灯；当距离小于15cm 时视为危险 |
## ch08_综合案例使用Jetson开发AI视觉机器人

| 文件 | 页码 | 类型 | 书中上下文 |
|---|---|---|---|
| `p227-228-229_01_import.py` | 227-228-229 | Python | 封装与扩展。 ／ 在代码实现层面，我们来构建一个L298N 电机控制器MotorController，便于后续功能 |
| `p229_01_def__override_pwm_destructor.py` | 229 | Python | 为。 ／ GPIO 清理流程冲突（导致“坏文件描述符”错误），因此通过覆写析构函数禁用这一自动行 |
| `p229_02_def_set_motor_direction.py` | 229 | Python | 高低位信号，控制电机转动方向。 ／ 这里构建电机转向控制实现方法set_motor_direction，通过控制L298N 的IN1 ～IN4 |
| `p229-230_01_def_set_motor_speed.py` | 229-230 | Python | 脚PWM 信号，控制电机转速。 ／ 这里构建电机转速控制实现方法set_motor_speed，通过控制L298N 的ENA、ENB 引 |
| `p230-231_01_def_car_forward.py` | 230-231 | Python | 停止等。 ／ 有了前面的基本实现，就可以构建小车完整的运动控制：前进、后退、左转、右转、 |
| `p231-232_01_def_cleanup.py` | 231-232 | Python | 最后，释放GPIO 资源。 |
| `p232_01_if___name.py` | 232 | Python | 可以参考如下程序，使用Jetson 驱动L298N 两路电机控制。 |
| `p233_01_import.py` | 233 | Python | 位置偏差。 ／ 识别指定类别的目标并计算其与屏幕中心的 |
| `p233-234_01_class_ObjectDetector.py` | 233-234 | Python | 图8-6Jetson-Inference 目标检测 ／ 位置偏差。 |
| `p234-235-236_01_def_process_frame.py` | 234-235-236 | Python | 添加各种可视化元素并显示图像。 ／ 与屏幕中心的偏移量，将图像转换为 OpenCV 兼容的格式并调整大小，最后调用绘图函数 |
| `p236-237-238_01_def__draw_overlay.py` | 236-237-238 | Python | 比例适应显示窗口，保持良好的视觉效果。 ／ 键信息。这些视觉元素帮助用户直观了解检测情况，而_resize_image 方法则确保图像能按 |
| `p238-239_01_def_start_detection.py` | 238-239 | Python | 性，又提供了灵活的操作接口，使得该类能够适应多种应用场景。 ／ 提供了单帧检测的功能，满足不同场景下的使用需求。整体设计既考虑了实时检测的连续 |
| `p239_01_if___name.py` | 239 | Python | 最后，参考如下代码，启动目标检测器。 |
| `p239-240_01_import.py` | 239-240 | Python | ObjectDetector（Jetson-Inference 目标检测）两个工具类，最终实现AI 视觉控制两轮机器人。 ／ 里构建核心控制类TargetTra |
| `p241-242_01_def__decision_making.py` | 241-242 | Python | 导致的频繁启停，提升跟踪稳定性。 ／ 对于未检测到目标的情况，系统会通过计时判断是否超过设定延迟，避免因短暂遮挡 |
| `p242-243_01_def_start_tracking.py` | 242-243 | Python | 免硬件故障和资源占用问题。 ／ 异常情况下通过 stop_tracking 方法安全停止，释放电机 GPIO 资源和摄像头设备，避 |

## 类型统计

- Shell: 147
- Python: 81
- 终端输出: 6
- 文本: 5
- desktop: 3
- Dockerfile: 3
- XML: 1
- C++: 1
- 配置: 1
