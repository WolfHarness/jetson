# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第089页 (PDF第99页)
# 上下文: 执行以下代码测试PyTorch 是否支持GPU 加速。 ／ 2. 测试PyTorch

# 验证PyTorch是否支持GPU加速
python3 -c "import torch; print('PyTorch GPU Available:', torch.cuda.is_available())"
