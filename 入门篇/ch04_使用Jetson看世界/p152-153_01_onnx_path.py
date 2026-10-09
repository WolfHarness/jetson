# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第152-153页 (PDF第162页, PDF第163页)
# 上下文: 接下来将“resnet_cat_dog_classifier.pth”转换为“resnet_cat_dog_model.onnx”。 ／ 首先加载模型，参考如下

# 将模型转换为ONNX格式
onnx_path = 'resnet_cat_dog_model.onnx'
torch.onnx.export(model, dummy_input, onnx_path, verbose=True, input_names=['input'], output_names=['output'])

print(f"Model has been saved as '{onnx_path}'")
