# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第080页 (PDF第90页)
# 上下文: 加速是否可用，具体内容如下。 ／ 构建一个名为“ opencv_cuda_check.cpp”的C++ 文件，用于检测OpenCV 使用GPU

/**
 * 测试OpenCV使用GPU加速是否可用
 */

#include <opencv2/opencv.hpp>
#include <opencv2/core/cuda.hpp>

int main() {
    // 加载CUDA模块
    cv::cuda::printShortCudaDeviceInfo(cv::cuda::getDevice());

    // 检查CUDA设备并打印信息
    int deviceCount = cv::cuda::getCudaEnabledDeviceCount();
    if (deviceCount > 0) {
        std::cout << "OpenCV with CUDA: Yes" << std::endl;
        for (int i = 0; i < deviceCount; ++i) {
            cv::cuda::setDevice(i);
            cv::cuda::printCudaDeviceInfo(i);
        }
    } else {
        std::cout << "OpenCV with CUDA: No" << std::endl;
    }

    return 0;
}
