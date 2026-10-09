# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第140页 (PDF第150页)
# 上下文: 将模型保存下来以便后续使用，可参考如下代码。 ／ 8. 保存模型

# Step 8: 保存模型
torch.save(net.state_dict(), 'final_model_weights.pth')  # 保存模型权重
