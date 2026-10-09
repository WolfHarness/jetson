# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第165页 (PDF第175页)
# 上下文: 接下来对参数进行解析，并为网络参数设置默认值。 ／ jetson_utils。

    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="filename of the image to
process")
    parser.add_argument("--network", type=str, default="googlenet", help="model
to use, can be: googlenet, resnet-18, ect.")
    args = parser.parse_args()
