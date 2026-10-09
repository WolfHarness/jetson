# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第151页 (PDF第161页)
# 上下文: 最后，构建一个函数用于图片展示。

# 展示分组后的图像
def plot_prediction_collections(model, data_loader, class_names, num_samples=4, save_path='prediction_results.png'):
    correct_images, incorrect_images, correct_titles, incorrect_titles, correct_preds, incorrect_preds = group_predictions(model, data_loader, class_names, num_samples)

    fig, axs = plt.subplots(2, num_samples, figsize=(15, 6))
    fig.suptitle('Correct and Incorrect Predictions', fontsize=16)

    # 展示正确预测
    for i in range(len(correct_images)):
        imshow(axs[0, i], correct_images[i], f'Pred: {correct_preds[i]}, Actual: {correct_titles[i]}')

    # 展示错误预测
    for i in range(len(incorrect_images)):
        imshow(axs[1, i], incorrect_images[i], f'Pred: {incorrect_preds[i]}, Actual: {incorrect_titles[i]}')

    plt.tight_layout()
    plt.savefig(save_path)  # 保存图片
    plt.show()
