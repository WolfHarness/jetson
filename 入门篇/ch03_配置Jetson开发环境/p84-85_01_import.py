# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第84-85页 (PDF第94页, PDF第95页)
# 上下文: 自动识别GPU 并使用GPU 运算。 ／ 会尽可能智能地在可用的CPU 和GPU 之间分配操作。可以通过如下代码测试其是否能够

# 测试TensorFlow，验证GPU加速可用
import tensorflow as tf

# 检查是否有GPU可用
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    # 打印第一个GPU的名称
    gpu_device_name = gpus[0].name
    print('Using GPU:', gpu_device_name)

    # 允许TensorFlow动态增长显存使用
    tf.config.experimental.set_memory_growth(gpus[0], True)

    # 确保操作在GPU上执行
    with tf.device('/GPU:0'):
        x = tf.random.normal((3, 3))
        print("TensorFlow Tensor on GPU:")
        print(x)
        print("Device name:", x.device)
else:
    print('No GPU found. Using CPU instead.')
    x = tf.random.normal((3, 3))
    print("TensorFlow Tensor on CPU:")
    print(x)
    print("Device name:", x.device)
