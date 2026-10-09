# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第084页 (PDF第94页)
# 上下文: 通过执行以下代码来测试GPU 是否可用。 ／ 2. 测试TensorFlow

# 验证TensorFlow是否支持GPU加速
python3 -c "import tensorflow as tf; print('TensorFlow GPU Available: ', len(tf.config.list_physical_devices('GPU')) > 0)"
